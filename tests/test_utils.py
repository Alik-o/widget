from unittest.mock import patch

from src.utils import get_amount_transaction_rubles, get_financial_transaction_data


def test_get_financial_transaction_data():
    assert get_financial_transaction_data(r"./tests/test_operations.json") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]


def test_get_financial_transaction_data_error():
    with patch("builtins.open", side_effect=Exception):
        assert get_financial_transaction_data("non_existent_file.json") == []


def test_get_amount_transaction_rubles(transactions):
    assert get_amount_transaction_rubles(transactions[2]) == "43318.34"


@patch("src.utils.get_currency_conversion")
def test_get_amount_transaction_rubles_conversion(mock_conversion):
    mock_conversion.return_value = 10000
    assert (
        get_amount_transaction_rubles(
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        )
        == 10000
    )
    mock_conversion.assert_called_once_with("USD", "9824.07", "2018-06-30")
