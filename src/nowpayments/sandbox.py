"""
A Python wrapper for the NOWPayments API Sandbox.
"""
from src.nowpayments import NOWPayments


class NOWPaymentsSandbox(NOWPayments):
    """
    Class to used for the NOWPayments API Sandbox.
    """

    API_URL = "https://api.sandbox.nowpayments.io/v1/{}"
