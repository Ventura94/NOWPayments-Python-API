"""
A Python wrapper for the NOWPayments API Sandbox.
"""
from typing import Union, Dict
from requests.exceptions import HTTPError
from nowpayments import NOWPayments


class NOWPaymentsSandbox(NOWPayments):
    """
    Class to used for the NOWPayments API Sandbox.
    """

    # This has recently been changed from https://api.sandbox.nowpayments.io/v1/ to this.
    API_URL = "https://api-sandbox.nowpayments.io/v1/{}"
    IS_SANDBOX = True
