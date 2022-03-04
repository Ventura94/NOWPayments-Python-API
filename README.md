# NOWPayments-Python-API

[![CodeQL](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/codeql-analysis.yml)
[![Pylint](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/pylint.yml/badge.svg)](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/pylint.yml)
[![Python application](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/python-app.yml/badge.svg)](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/python-app.yml)
[![Python package](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/python-package.yml/badge.svg)](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/python-package.yml)
[![Upload Python Package](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/python-publish.yml/badge.svg)](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/python-publish.yml)
[![codecov](https://codecov.io/gh/Ventura94/NOWPayments-Python-API/branch/main/graph/badge.svg?token=Z7NIDJI2LD)](https://codecov.io/gh/Ventura94/NOWPayments-Python-API)
[![Black](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/black.yml/badge.svg)](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/black.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python wrapper for the [NOWPayments API](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest). 

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
Sandbox is used in the same way in correspondence with the documentation as follows.
```python
from nowpayments.sandbox import NOWPaymentsSandbox
payment = NOWPaymentsSandbox("SANDBOX_API_KEY")

status = payment.get_status()
```



