"""
Dataclasses for the NowPayments API.
"""
from inspect import signature
from typing import Dict, Union
from dataclasses import dataclass


@dataclass
class PaymentData:  # pylint: disable=too-many-instance-attributes
    """
    The PaymentData class is a container for the data that is used to make a payment.
    """
    price_amount: float
    price_currency: str
    pay_amount: float
    pay_currency: str
    ipn_callback_url: str
    order_id: str
    order_description: str
    purchase_id: int
    payout_address: str
    payout_currency: str
    payout_extra_id: str
    fixed_rate: bool
    case: str

    def clean_data_to_dict(
            self, is_sandbox: bool = False
    ) -> Dict[str, Union[str, float, int]]:
        """
        Delete None types and return dictionary
        """
        data = {}
        for field in signature(self.__class__).parameters:
            if getattr(self, field):
                data[field] = getattr(self, field)
            else:
                data[field] = None
        if is_sandbox and data.get("case") is None:
            data["case"] = "success"
        else:
            del data["case"]
        return data
