import requests


class NOWPayments:
    API_URL = "https://api.nowpayments.io/v1/{}"
    ESTIMATE_AMOUNT_URL = "estimate?amount={}&currency_from={}&currency_to={}"
    MIN_AMOUNT_URL = "min-amount?currency_from={}&currency_to={}"

    def __init__(self, key):
        self.key = key

    def get_url(self, endpoint):
        return self.API_URL.format(endpoint)

    def get_status(self):
        endpoint = "status"
        url = self.get_url(endpoint)
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_requests(self, url):
        headers = {'x-api-key': self.key}
        return requests.get(url=url, headers=headers)

    def post_requests(self, url, data=None):
        headers = {'x-api-key': self.key}
        return requests.post(url=url, headers=headers, data=data)

    def get_currencies(self):
        endpoint = "currencies"
        url = self.get_url(endpoint)
        resp = self.get_requests(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_estimate_amount(self, amount=None, currency_from="usd", currency_to="btc"):
        endpoint = self.ESTIMATE_AMOUNT_URL.format(amount, currency_from, currency_to)
        url = self.get_url(endpoint)
        resp = self.get_requests(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_payment(self, price_amount=None, price_currency="usd", pay_amount=None, pay_currency="btc",
                    ipn_callback_url=None, order_id=None, order_description=None, buy_id=None, payout_address=None,
                    payout_currency=None, payout_extra_id=None, fixed_rate=None):
        endpoint = "payment"
        data = {
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

        url = self.get_url(endpoint)
        resp = self.post_requests(url, data=data)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_payment_status(self, payment_id):
        endpoint = "payment/{}".format(payment_id)
        url = self.get_url(endpoint)
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_min_amount(self, currency_from=None, currency_to=None):
        endpoint = self.MIN_AMOUNT_URL.format(currency_from, currency_to)
        url = self.get_url(endpoint)
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text


pay = NOWPayments(key="RF0Q129-AWN408R-HC9N8CR-CH95SBA")
pay_dic = pay.get_payment(price_amount="100")
print(pay_dic)
