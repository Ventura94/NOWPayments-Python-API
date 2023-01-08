"""
A Python wrapper for the NOWPayments API Sandbox.
"""
from nowpayments import NOWPayments


class NOWPaymentsSandbox(NOWPayments):
    """
    Class to used for the NOWPayments API Sandbox.
    """

    # This has recently been changed from https://api.sandbox.nowpayments.io/v1/ to this.
    _API_URL = "https://api-sandbox.nowpayments.io/v1/{}"
    _IS_SANDBOX = True
