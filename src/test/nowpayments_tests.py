import os
import unittest
from src.nowpayments import NOWPayments


class NOWPaymentsTest(unittest.TestCase):

    def setUp(self):
        self.now_payments = NOWPayments(
            key=os.environ['API_KEY']
        )

    def test_get_api_status(self):
        self.assertEqual(self.now_payments.get_api_status(), {'message': 'OK'})

    def test_get_available_currencies(self):
        self.assertEqual(self.now_payments.get_available_currencies().keys(),
                         {'currencies': ''}.keys())


if __name__ == '__main__':
    unittest.main()
