import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions):
    function_calling = filter_by_currency(transactions, "USD")
    assert next(function_calling) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(function_calling) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(function_calling) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_filter_by_currency_no_transfer_currency(transactions):
    with pytest.raises(ValueError):
        next(filter_by_currency(transactions))


def test_filter_by_currency_no_list(no_data):
    with pytest.raises(StopIteration):
        next(filter_by_currency(no_data, "USD"))


def test_transaction_descriptions(transactions):
    function_calling = transaction_descriptions(transactions)
    assert next(function_calling) == "Перевод организации"
    assert next(function_calling) == "Перевод со счета на счет"


def test_transaction_descriptions_no_list(no_data):
    with pytest.raises(StopIteration):
        next(transaction_descriptions(no_data))


def test_card_number_generator():
    generator = card_number_generator(1, 3)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"


def test_card_number_generator_limit_numbers():
    with pytest.raises(ValueError):
        next(card_number_generator(10_000_000_000_000_000, 10_000_000_000_000_002))
