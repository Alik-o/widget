import json
import logging
from typing import Any

from src.external_api import get_currency_conversion

logger_transaction_data = logging.getLogger("transaction_data")
logger_amount_transaction = logging.getLogger("amount_transaction")
logger_transaction_data.setLevel(logging.DEBUG)
logger_amount_transaction.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger_amount_transaction.addHandler(file_handler)
logger_transaction_data.addHandler(file_handler)


def get_financial_transaction_data(path_to: str) -> Any:
    """Возвращает список словарей с данными о финансовых транзакциях"""

    try:
        logger_transaction_data.info("Получен путь до json файла")
        with open(path_to, encoding="utf-8") as f:
            data = json.load(f)
        logger_transaction_data.info("json файл распакован удачно")
        return data
    except Exception as ex:
        logger_transaction_data.warning(ex)
        return list()


def get_amount_transaction_rubles(transactions: dict) -> float:
    """Возвращает сумму транзакции в рублях, если транзакция была не в рублях то конвертирует в рубли"""
    logger_amount_transaction.info("Получены данные о транзакции")
    currency = transactions["operationAmount"]["currency"]["code"]
    amount = transactions["operationAmount"]["amount"]
    logger_amount_transaction.info("Проверка валюты транзакции")
    if currency != "RUB":
        logger_amount_transaction.info(f"Транзакция была в {currency}, отправка на конвертацию в рубли")
        date = transactions["date"][:10]
        amount = get_currency_conversion(currency, amount, date)
    logger_amount_transaction.info("Получена сумма в рублях")
    return amount


if __name__ == "__main__":
    transaction = get_financial_transaction_data(r"..\data\operations.json")
    print(get_amount_transaction_rubles(transaction[1]))
