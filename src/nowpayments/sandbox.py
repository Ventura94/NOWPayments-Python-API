"""
A Python wrapper for the NOWPaiments API Sandbox.
"""
from typing import Any

import requests
from requests import Response


class NOWPayments:
    """
    Class to used for the NOWPaiments API Sandbox.
    """

    API_URL: str = "https://api.sandbox.nowpayments.io/v1/{}"
    ESTIMATE_AMOUNT_URL: str = "estimate?amount={}&currency_from={}&currency_to={}"
    MIN_AMOUNT_URL: str = "min-amount?currency_from={}&currency_to={}"

    def __init__(self, key: str) -> None:
        """
        Class construct. Receives your api key as initial parameter.

        :param str key: API key
        """
        self.key: str = key

    def get_url(self, endpoint: str) -> str:
        """
        Set the url to be used

        :param str endpoint: Endpoint to be used
        """
        return self.API_URL.format(endpoint)

    def get_requests(self, url: str) -> Response:
        """
        Make get requests with your header

        :param str url: URL to which the request is made
        """
        headers: dict = {"x-api-key": self.key}
        return requests.get(url=url, headers=headers)

    def post_requests(self, url: str, data: dict = None) -> Response:
        """
        Make get requests with your header and data

        :param url: URL to which the request is made
        :param data: Data to which the request is made
        """
        headers: dict = {"x-api-key": self.key}
        return requests.post(url=url, headers=headers, data=data)

    def get_api_status(self) -> Any:
        """
        This is a method to get information about the current state of the API. If everything
        is OK, you will receive an "OK" message. Otherwise, you'll see some error.
        """
        endpoint: str = "status"
        url: str = self.get_url(endpoint)
        resp: Response = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        return resp.text

    def get_available_currencies(self) -> Any:
        """
        This is a method for obtaining information about all cryptocurrencies available for
        payments.
        """
        endpoint: str = "currencies"
        url: str = self.get_url(endpoint)
        resp: Response = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        return resp.text

    def get_available_checked_currencies(self) -> Any:
        """
        This is a method for obtaining information about the cryptocurrencies available
         for payments. Shows the coins you set as available for payments in the "coins settings"
          tab on your personal account.
        """
        endpoint: str = "merchant/coins"
        url: str = self.get_url(endpoint)
        resp: Response = self.get_requests(url)
        if resp.status_code == 200:
            return resp.json()
        return resp.text

    def get_estimate_price(
        self, amount: float, currency_from: str, currency_to: str
    ) -> Any:
        """This is a method for calculating the approximate price in cryptocurrency
        for a given value in Fiat currency. You will need to provide the initial cost
         in the Fiat currency (amount, currency_from) and the necessary cryptocurrency
         (currency_to) Currently following fiat currencies are available: usd, eur, nzd,
          brl, gbp.

         :param  float amount: Cost value.

         :param  str currency_from: Fiat currencies.

         :param  str currency_to: Cryptocurrency.
        """
        endpoint: str = self.ESTIMATE_AMOUNT_URL.format(
            amount, currency_from, currency_to
        )
        url: str = self.get_url(endpoint)
        resp: Response = self.get_requests(url)
        if resp.status_code == 200:
            return resp.json()
        return resp.text

    def create_payment(
        self, price_amount: float, price_currency: str, pay_currency: str, **kwargs: Any
    ) -> Any:
        """
        With this method, your customer will be able to complete the payment without leaving
        your website.

        :param float price_amount: The fiat equivalent of the price to be paid in crypto.

        :param str price_currency: The fiat currency in which the price_amount is specified.

        :param str pay_currency: The crypto currency in which the pay_amount is specified.

        :param float pay_amount: The amount that users have to pay for the order stated in crypto.

        :param str ipn_callback_url: Url to receive callbacks, should contain "http" or "https".

        :param str order_id: Inner store order ID.

        :param str order_description: Inner store order description.

        :param int purchase_id: Id of purchase for which you want to create aother payment.

        :param str payout_address: Receive funds on another address.

        :param str payout_currency: Currency of your external payout_address.

        :param int payout_extra_id: Extra id or memo or tag for external payout_address.

        :param bool fixed_rate: Required for fixed-rate exchanges.
        """
        endpoint: str = "payment"
        data: dict = {
            "price_amount": price_amount,
            "price_currency": price_currency,
            "pay_amount": None,
            "pay_currency": pay_currency,
            "ipn_callback_url": None,
            "order_id": None,
            "order_description": None,
            "buy_id": None,
            "payout_address": None,
            "payout_currency": None,
            "payout_extra_id": None,
            "fixed_rate": None,
        }
        data.update(kwargs)
        if len(data) != 12:
            raise TypeError("create_payment() got an unexpected keyword argument")

        url: str = self.get_url(endpoint)
        resp: Response = self.post_requests(url, data=data)
        if resp.status_code == 200:
            return resp.json()
        return resp.text

    def get_payment_status(self, payment_id: int) -> str:
        """
        Get the actual information about the payment.

        :param int payment_id: ID of the payment in the request.
        """
        endpoint: str = f"payment/{payment_id}"
        url: str = self.get_url(endpoint)
        resp: Response = self.get_requests(url)
        if resp.status_code == 200:
            return resp.json()
        return resp.text

    def get_minimum_payment_amount(
        self, currency_from: str, currency_to: str = None
    ) -> str:
        """
        Get the minimum payment amount for a specific pair.

        :param currency_from: Currency from
        :param currency_to: Currency to
        """
        endpoint: str = self.MIN_AMOUNT_URL.format(currency_from, currency_to)
        url: str = self.get_url(endpoint)
        resp: Response = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        return resp.text
