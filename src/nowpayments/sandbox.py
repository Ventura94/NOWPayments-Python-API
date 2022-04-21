"""
A Python wrapper for the NOWPayments API Sandbox.
"""
from nowpayments import NOWPayments


class NOWPaymentsSandbox(NOWPayments):
    """
    Class to used for the NOWPayments API Sandbox.
    """

    ### This has recently been changed from https://api.sandbox.nowpayments.io/v1/ to this.
    API_URL = "https://api-sandbox.nowpayments.io/v1/"

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

        :param str case: Used to change the outcome of the payment, defaults to "success" other options are "fail" and "partially_paid"

        refer to https://documenter.getpostman.com/view/7907941/T1LSCRHC
        """
        endpoint = "payment"
        data = {
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
            "case": "success"
        }
        data.update(**kwargs)
        if len(data) != 13:
            raise TypeError("create_payment() got an unexpected keyword argument")

        url = self.get_url(endpoint)
        resp = self.post_requests(url, data=data)
        if resp.status_code == 201:
            return resp.json()
        raise HTTPError(
            f'Error {resp.status_code}: {resp.json().get("message", "Not descriptions")}'
        )
