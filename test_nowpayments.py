"""Testing Module"""
import os
import pytest
from requests.exceptions import HTTPError

import nowpayments
from src.nowpayments import NOWPayments


@pytest.fixture
def now_payments():
    return NOWPayments(key=os.environ["API_KEY"])


def test_api_url_param(now_payments):
    assert now_payments.API_URL == "https://api.nowpayments.io/v1/{}"


def test_estimate_amount_url_param(now_payments):
    assert now_payments.ESTIMATE_AMOUNT_URL == "estimate?amount={}&currency_from={}&currency_to={}"


def test_min_amount_url_param(now_payments):
    assert now_payments.MIN_AMOUNT_URL == "min-amount?currency_from={}&currency_to={}"


def test_get_url(now_payments):
    assert now_payments.get_url("endpoint") == "https://api.nowpayments.io/v1/endpoint"


def test_get_requests(now_payments):
    response = now_payments.get_requests("https://api.nowpayments.io/v1/status")
    assert response.status_code == 200


def test_get_api_status(now_payments, mocker):
    mocker.patch.object(NOWPayments,
                        "get_url",
                        return_value="https://api.nowpayments.io/v1/status",
                        autospec=True)
    assert now_payments.get_api_status() == {"message": "OK"}


def test_get_available_currencies(now_payments, mocker):
    mocker.patch.object(NOWPayments,
                        "get_url",
                        return_value="https://api.nowpayments.io/v1/currencies",
                        autospec=True)
    assert now_payments.get_available_currencies().get("currencies", "Not found") != "Not found"


def test_get_available_checked_currencies(now_payments, mocker):
    mocker.patch.object(NOWPayments,
                        "get_url",
                        return_value="https://api.nowpayments.io/v1/merchant/coins",
                        autospec=True)
    result = now_payments.get_available_checked_currencies()
    assert result.get('selectedCurrencies', 'Not found') != 'Not found'


def test_get_estimate_price(now_payments, mocker):
    mocker.patch.object(NOWPayments,
                        "get_url",
                        return_value="https://api.nowpayments.io/v1/estimate?amount=100&currency_from=usd&currency_to=btc",
                        autospec=True)
    result = now_payments.get_estimate_price(amount=100,
                                             currency_from="usd",
                                             currency_to="btc")
    assert result.get('estimated_amount', 'Not found') != 'Not found'


def test_get_estimate_price_error(now_payments, mocker):
    mocker.patch.object(NOWPayments,
                        "get_url",
                        return_value="https://api.nowpayments.io/v1/estimate?amount=100&currency_from=cup&currency_to=btc",
                        autospec=True)
    with pytest.raises(HTTPError, match="Error 404: Currency cup not found"):
        now_payments.get_estimate_price(amount=100, currency_from="cup", currency_to="eur")
