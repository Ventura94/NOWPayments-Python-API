# NOWPayments-Python-API

A Python wrapper for the [NOWPaiments API](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest). 

The api call descriptions are from the official documentation.

## Getting Started
Before using the NOWPayments API, sign up for a [free API key here](https://nowpayments.io/).

To install the wrapper, enter the following into the terminal.
```bash
pip install nowpayments
```

Every api call requires this api key. Make sure to use this key when getting started. 
```python
from nowpayments import NOWPayments
payment = NOWPayments("API_KEY")

status = payment.get_status()
```



