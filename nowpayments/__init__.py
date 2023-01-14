"""
A Python wrapper for the NOWPayments API.
"""
from typing import Any, Dict, Union

import requests
from nowpayments.models.payment import PaymentData
from requests import Response
from requests.exceptions import HTTPError


class NOWPayments:
    """
    Class to used for the NOWPayments API.
    """

    _API_URL = "https://api.nowpayments.io/v1/{}"
    _ESTIMATE_AMOUNT_URL = "estimate?amount={}&currency_from={}&currency_to={}"
    _MIN_AMOUNT_URL = "min-amount?currency_from={}"
    _IS_SANDBOX = False

    def __init__(self, key: str) -> None:
        """
        Class construct. Receives your api key as initial parameter.

        :param str key: API key
        """
        self.session = requests.Session()
        self.key = key

    def _get_url(self, endpoint: str) -> str:
        """
        Set the url to be used

        :param str endpoint: Endpoint to be used
        """
        return self._API_URL.format(endpoint)

    def _get_requests(self, url: str) -> Response:
        """
        Make get requests with your header

        :param str url: URL to which the request is made
        """
        headers = {"x-api-key": self.key}
        return self.session.get(url=url, headers=headers)

    def _post_requests(self, url: str, data: Dict = None) -> Response:
        """
        Make get requests with your header and data

        :param url: URL to which the request is made
        :param data: Data to which the request is made
        """
        headers = {"x-api-key": self.key}
        return self.session.post(url=url, headers=headers, data=data)

    def get_api_status(self) -> Dict:
        """
        This is a method to get information about the current state of the API. If everything
        is OK, you will receive an "OK" message. Otherwise, you'll see some error.
        """
        endpoint = "status"
        url = self._get_url(endpoint)
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        raise HTTPError(
            f'Error {resp.status_code}: {resp.json().get("message", "Not descriptions")}'
        )

    def get_available_currencies(self) -> Dict:
        """
        This is a method for obtaining information about all cryptocurrencies available for
        payments.
        """
        endpoint = "currencies"
        url = self._get_url(endpoint)
        resp = self._get_requests(url)
        if resp.status_code == 200:
            return resp.json()
        raise HTTPError(
            f'Error {resp.status_code}: {resp.json().get("message", "Not descriptions")}'
        )

    def get_available_checked_currencies(self) -> Dict:
        """
        This is a method for obtaining information about the cryptocurrencies available
         for payments. Shows the coins you set as available for payments in the "coins settings"
          tab on your personal account.
        """
        endpoint = "merchant/coins"
        url = self._get_url(endpoint)
        resp = self._get_requests(url)
        if resp.status_code == 200:
            return resp.json()
        raise HTTPError(
            f'Error {resp.status_code}: {resp.json().get("message", "Not descriptions")}'
        )

    def get_estimate_price(
        self, amount: float, currency_from: str, currency_to: str
    ) -> Dict:
        """This is a method for calculating the approximate price in cryptocurrency
        for a given value in Fiat currency. You will need to provide the initial cost
         in the Fiat currency (amount, currency_from) and the necessary cryptocurrency
         (currency_to) Currently following fiat currencies are available: usd, eur, nzd,
          brl, gbp.

         :param  float amount: Cost value.

         :param  str currency_from: Fiat currencies.

         :param  str currency_to: Cryptocurrency.
        """
        endpoint = self._ESTIMATE_AMOUNT_URL.format(amount, currency_from, currency_to)
        url = self._get_url(endpoint)
        resp: Response = self._get_requests(url)
        if resp.status_code == 200:
            return resp.json()
        raise HTTPError(
            f'Error {resp.status_code}: {resp.json().get("message", "Not descriptions")}'
        )

    def create_payment(
        self,
        price_amount: float,
        price_currency: str,
        pay_currency: str,
        **kwargs: Union[str, float, bool, int],
    ) -> Dict:
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

        :param int purchase_id: Id of purchase for which you want to create a other payment.

        :param str payout_address: Receive funds on another address.

        :param str payout_currency: Currency of your external payout_address.

        :param int payout_extra_id: Extra id or memo or tag for external payout_address.

        :param bool fixed_rate: Required for fixed-rate exchanges.
        """
        endpoint = "payment"
        data = PaymentData(
            price_amount=price_amount,
            price_currency=price_currency,
            pay_currency=pay_currency,
            **kwargs,
        )
        url = self._get_url(endpoint)
        resp = self._post_requests(
            url, data=data.clean_data_to_dict(is_sandbox=self._IS_SANDBOX)
        )
        if resp.status_code == 201:
            return resp.json()
        raise HTTPError(
            f'Error {resp.status_code}: {resp.json().get("message", "Not descriptions")}'
        )

    def get_payment_status(self, payment_id: int) -> Any:
        """
        Get the actual information about the payment.

        :param int payment_id: ID of the payment in the request.
        """
        endpoint = f"payment/{payment_id}"
        url = self._get_url(endpoint)
        resp: Response = self._get_requests(url)
        if resp.status_code == 200:
            return resp.json()
        raise HTTPError(
            f'Error {resp.status_code}: {resp.json().get("message", "Not descriptions")}'
        )

    def get_minimum_payment_amount(
        self, currency_from: str, currency_to: str = None, fiat_equivalent: str = None
    ) -> Any:
        """
        Get the minimum payment amount for a specific pair.

        :param currency_from: Currency from
        :param currency_to: Currency to
        """
        endpoint = self._MIN_AMOUNT_URL.format(currency_from)
        if currency_to is not None:
            endpoint += f"&currency_to={currency_to}"
        if fiat_equivalent is not None:
            endpoint += f"&fiat_equivalent={fiat_equivalent}"
        url = self._get_url(endpoint)
        resp: Response = self._get_requests(url)
        if resp.status_code == 200:
            return resp.json()
        raise HTTPError(
            f'Error {resp.status_code}: {resp.json().get("message", "Not descriptions")}'
        )
