"""
A Python wrapper for the NOWPaiments API Sandbox.
"""
from src.nowpayments import NOWPayments


class NOWPaymentsSandbox(NOWPayments):
    """
    Class to used for the NOWPaiments API Sandbox.
    """

    API_URL = "https://api.sandbox.nowpayments.io/v1/{}"
