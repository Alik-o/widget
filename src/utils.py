import json
import os

def financial_transaction_data(path_to: str) -> list:
    """Возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path_to, encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception:
        return list()


if __name__ == '__main__':
    print(financial_transaction_data(r".Д./data/operations.json"))
