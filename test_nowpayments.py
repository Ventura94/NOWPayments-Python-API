"""Testing Module"""
import os
import pytest
from pytest_mock.plugin import MockerFixture
from requests.exceptions import HTTPError
from src.nowpayments import NOWPayments


@pytest.fixture
def now_payments() -> NOWPayments:
    """
    NOWPayments class fixture.
    :return: NOWPayments class.
    """
    return NOWPayments(key=os.environ["API_KEY"])


def test_api_url_param(
    now_payments: NOWPayments,  # pylint: disable=redefined-outer-name
) -> None:
    """
    API url param test
    :param now_payments: NOWPayments class fixture
    :return:
    """
    assert now_payments.API_URL == "https://api.nowpayments.io/v1/{}"


def test_estimate_amount_url_param(
    now_payments: NOWPayments,  # pylint: disable=redefined-outer-name
) -> None:
    """
    Estimate amount url param test.
    """
    assert (
        now_payments.ESTIMATE_AMOUNT_URL
        == "estimate?amount={}&currency_from={}&currency_to={}"
    )


def test_min_amount_url_param(
    now_payments: NOWPayments,  # pylint: disable=redefined-outer-name
) -> None:
    """
    Min amount url param test.
    """
    assert now_payments.MIN_AMOUNT_URL == "min-amount?currency_from={}&currency_to={}"


def test_get_url(
    now_payments: NOWPayments,  # pylint: disable=redefined-outer-name
) -> None:
    """
    Get URL test
    """
    assert now_payments.get_url("endpoint") == "https://api.nowpayments.io/v1/endpoint"


def test_get_requests(
    now_payments: NOWPayments,  # pylint: disable=redefined-outer-name
) -> None:
    """
    Get request test
    """

    response = now_payments.get_requests("https://api.nowpayments.io/v1/status")
    assert response.status_code == 200


def test_get_api_status(
    now_payments: NOWPayments,  # pylint: disable=redefined-outer-name
    mocker: MockerFixture,
) -> None:
    """
    Get api status test
    """
    mocker.patch.object(
        NOWPayments,
        "get_url",
        return_value="https://api.nowpayments.io/v1/status",
        autospec=True,
    )
    assert now_payments.get_api_status() == {"message": "OK"}


def test_get_available_currencies(
    now_payments: NOWPayments,  # pylint: disable=redefined-outer-name
    mocker: MockerFixture,
) -> None:
    """
    Get available currencies test.
    """
    mocker.patch.object(
        NOWPayments,
        "get_url",
        return_value="https://api.nowpayments.io/v1/currencies",
        autospec=True,
    )
    assert (
        now_payments.get_available_currencies().get("currencies", "Not found")
        != "Not found"
    )


def test_get_available_checked_currencies(
    now_payments: NOWPayments,  # pylint: disable=redefined-outer-name
    mocker: MockerFixture,
) -> None:
    """
    Get available checked currencies test
    """
    mocker.patch.object(
        NOWPayments,
        "get_url",
        return_value="https://api.nowpayments.io/v1/merchant/coins",
        autospec=True,
    )
    result = now_payments.get_available_checked_currencies()
    assert result.get("selectedCurrencies", "Not found") != "Not found"


def test_get_estimate_price(
    now_payments: NOWPayments,  # pylint: disable=redefined-outer-name
    mocker: MockerFixture,
) -> None:
    """
    Get estimate price test.
    """
    mocker.patch.object(
        NOWPayments,
        "get_url",
        return_value="https://api.nowpayments.io/v1/estimate?amount=\
        100&currency_from=usd&currency_to=btc",
        autospec=True,
    )
    result = now_payments.get_estimate_price(
        amount=100, currency_from="usd", currency_to="btc"
    )
    assert result.get("estimated_amount", "Not found") != "Not found"


def test_get_estimate_price_error(
    now_payments: NOWPayments,  # pylint: disable=redefined-outer-name
    mocker: MockerFixture,
) -> None:
    """
    Get estimate price test with error.
    """
    mocker.patch.object(
        NOWPayments,
        "get_url",
        return_value="https://api.nowpayments.io/v1/estimate?amount=\
        100&currency_from=cup&currency_to=btc",
        autospec=True,
    )
    with pytest.raises(HTTPError, match="Error 404: Currency cup not found"):
        now_payments.get_estimate_price(
            amount=100, currency_from="cup", currency_to="eur"
        )


def test_create_payment_unexpected_keyword_argument_error(
    now_payments: NOWPayments,  # pylint: disable=redefined-outer-name
) -> None:
    """
    Create payment test with unexpected keyword argument error
    """
    with pytest.raises(TypeError):
        now_payments.create_payment(
            price_amount=100,
            price_currency="usd",
            pay_currency="btc",
            unexpected="argument",
        )


def test_create_payment(
    now_payments: NOWPayments,  # pylint: disable=redefined-outer-name
    mocker: MockerFixture,
) -> None:
    """
    Create payment test
    """
    mocker.patch.object(
        NOWPayments,
        "get_url",
        return_value="https://api.nowpayments.io/v1/payment",
        autospec=True,
    )
    result = now_payments.create_payment(
        price_amount=100, price_currency="usd", pay_currency="btc"
    )
    assert result.get("payment_id", "Not found") != "Not found"


def test_create_payment_with_argument(
    now_payments: NOWPayments,  # pylint: disable=redefined-outer-name
    mocker: MockerFixture,
) -> None:
    """
    Create payment test with argument
    """
    mocker.patch.object(
        NOWPayments,
        "get_url",
        return_value="https://api.nowpayments.io/v1/payment",
        autospec=True,
    )
    result = now_payments.create_payment(
        price_amount=100,
        price_currency="usd",
        pay_currency="btc",
        order_description="My order",
    )
    assert result.get("order_description", "Not found") == "My order"


def test_create_payment_with_error(
    now_payments: NOWPayments,  # pylint: disable=redefined-outer-name
    mocker: MockerFixture,
) -> None:
    """
    Create payment test with error
    """
    mocker.patch.object(
        NOWPayments,
        "get_url",
        return_value="https://api.nowpayments.io/v1/payment",
        autospec=True,
    )
    with pytest.raises(
        HTTPError,
        match="Error 500: This currency is currently unavailable. Try it in 2 hours",
    ):
        now_payments.create_payment(
            price_amount=100, price_currency="usd", pay_currency="cup"
        )
