import json
from typing import Any

from src.external_api import get_currency_conversion


def get_financial_transaction_data(path_to: str) -> Any:
    """Возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path_to, encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception:
        return list()


def get_amount_transaction_rubles(transactions: dict) -> float:
    """Возвращает сумму транзакции в рублях, если транзакция была не в рублях то конвертирует в рубли"""
    currency = transactions["operationAmount"]["currency"]["code"]
    amount = transactions["operationAmount"]["amount"]
    if currency != "RUB":
        date = transactions["date"][:10]
        amount = get_currency_conversion(currency, amount, date)
    return amount


# if __name__ == "__main__":
#     print(get_financial_transaction_data(r"../data/operations.json"))


if __name__ == "__main__":
    transactions = get_financial_transaction_data(r"../data/operations.json")
    print(transactions[2])
    print(get_amount_transaction_rubles(transactions[2]))
