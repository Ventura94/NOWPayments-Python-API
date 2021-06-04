# NOWPayments-Python-API

[![CodeQL](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/codeql-analysis.yml)
[![Upload Python Package](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/python-publish.yml/badge.svg)](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/python-publish.yml)

A Python wrapper for the [NOWPaiments API](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest). 

The api call descriptions are from the official documentation.

## Getting Started
Before using the NOWPayments API, sign up for a [API key here](https://nowpayments.io/).
If you want to use the Sandbox, request your [API key here](https://account.sandbox.nowpayments.io/).


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
Sanbox is used in the same way in correspondence with the documentation as follows.
```python
from nowpayments.sandbox import NOWPayments
payment = NOWPayments("API_KEY")

status = payment.get_status()
```



