import requests
from requests import Response




class NOWPayments:
    API_URL: str = "https://api.nowpayments.io/v1/{}"
    ESTIMATE_AMOUNT_URL: str = "estimate?amount={}&currency_from={}&currency_to={}"
    MIN_AMOUNT_URL: str = "min-amount?currency_from={}&currency_to={}"

    def __init__(self, key: str):
        self.key: str = key

    def get_url(self, endpoint: str) -> str:
        return self.API_URL.format(endpoint)

    def get_status(self) -> str:
        endpoint: str = "status"
        url: str = self.get_url(endpoint)
        resp: Response = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_requests(self, url: str) -> Response:
        headers: dict = {"x-api-key": self.key}
        return requests.get(url=url, headers=headers)

    def post_requests(self, url: str, data: dict = None) -> Response:
        headers: dict = {"x-api-key": self.key}
        return requests.post(url=url, headers=headers, data=data)

    def get_currencies(self) -> str:
        endpoint: str = "currencies"
        url: str = self.get_url(endpoint)
        resp: Response = self.get_requests(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_estimate_amount(
        self, amount: float = None, currency_from: str = "usd", currency_to: str = "btc"
    ) -> str:
        endpoint: str = self.ESTIMATE_AMOUNT_URL.format(
            amount, currency_from, currency_to
        )
        url: str = self.get_url(endpoint)
        resp: Response = self.get_requests(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_payment(
        self,
        price_amount: float = None,
        price_currency: str = "usd",
        pay_amount: float = None,
        pay_currency: str = "btc",
        ipn_callback_url: str = None,
        order_id: int = None,
        order_description: str = None,
        buy_id: int = None,
        payout_address: str = None,
        payout_currency: float = None,
        payout_extra_id: int = None,
        fixed_rate: str = None,
    ) -> str:
        endpoint: str = "payment"
        data: dict = {
            "price_amount": price_amount,
            "price_currency": price_currency,
            "pay_amount": pay_amount,
            "pay_currency": pay_currency,
            "ipn_callback_url": ipn_callback_url,
            "order_id": order_id,
            "order_description": order_description,
            "buy_id": buy_id,
            "payout_address": payout_address,
            "payout_currency": payout_currency,
            "payout_extra_id": payout_extra_id,
            "fixed_rate": fixed_rate,
        }

        url: str = self.get_url(endpoint)
        resp: Response = self.post_requests(url, data=data)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_payment_status(self, payment_id: int) -> str:
        endpoint: str = f"payment/{payment_id}"
        url: str = self.get_url(endpoint)
        resp: Response = self.get_requests(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_min_amount(self, currency_from: str = None, currency_to: str = None) -> str:
        endpoint: str = self.MIN_AMOUNT_URL.format(currency_from, currency_to)
        url: str = self.get_url(endpoint)
        resp: Response = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text
