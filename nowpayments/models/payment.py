"""
Dataclasses for the NowPayments API.
"""
from dataclasses import dataclass
from inspect import signature
from typing import Dict, Union


@dataclass
class PaymentData:  # pylint: disable=too-many-instance-attributes
    """
    The PaymentData class is a container for the data that is used to make a payment.
    """

    price_amount: float
    price_currency: str
    pay_currency: str
    pay_amount: float = None
    ipn_callback_url: str = None
    order_id: str = None
    order_description: str = None
    purchase_id: int = None
    payout_address: str = None
    payout_currency: str = None
    payout_extra_id: str = None
    fixed_rate: bool = None
    case: str = None

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
            #else:
            #    data[field] = None
        if is_sandbox and data.get("case") is None:
            data["case"] = "success"
        else:
            del data["case"]
        return data
