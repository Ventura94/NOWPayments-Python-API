import os
import pytest
from src.nowpayments import NOWPayments


@pytest.fixture
def now_payments():
    return NOWPayments(
        key=os.environ['API_KEY']
    )


def test_get_api_status(now_payments):
    assert now_payments.get_api_status() == {'message': 'OK'}


def test_get_available_currencies(now_payments):
    assert now_payments.get_available_currencies().keys() == {'currencies': ''}.keys()
