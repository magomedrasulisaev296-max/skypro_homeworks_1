from unittest.mock import patch
from src.external_api import get_transaction_amount_in_rub


def test_rub():
    assert get_transaction_amount_in_rub({"amount": "1000.50", "currency": "RUB"}) == 1000.50


def test_unknown():
    assert get_transaction_amount_in_rub({"amount": "500", "currency": "GBP"}) == 500.0


def test_missing():
    assert get_transaction_amount_in_rub({}) == 0.0


@patch('src.external_api.requests.get')
def test_usd(mock_get):
    mock_get.return_value.json.return_value = {"success": True, "result": 7500.50}
    assert get_transaction_amount_in_rub({"amount": "100", "currency": "USD"}) == 7500.50


@patch('src.external_api.requests.get')
def test_api_fail(mock_get):
    mock_get.return_value.json.return_value = {"success": False}
    assert get_transaction_amount_in_rub({"amount": "200", "currency": "USD"}) == 200.0


@patch('src.external_api.requests.get')
def test_network_error(mock_get):
    mock_get.side_effect = Exception()
    assert get_transaction_amount_in_rub({"amount": "300", "currency": "EUR"}) == 300.0