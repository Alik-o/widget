import re
from collections import Counter


def search_by_description(transactions_list: list, search_string: str) -> list:
    """Возвращает список словарей в которых есть искомая строка"""
    search_result_list = []
    for transaction in transactions_list:
        if transaction:
            if re.search(search_string, transaction.get("description"), flags=re.IGNORECASE):
                search_result_list.append(transaction)
    return search_result_list


def filter_by_category(transactions_list: list, category_list: list) -> dict:
    """Возвращает словарь с количеством операций по категориям"""
    category_counter = Counter([transactions.get("description") for transactions in transactions_list])
    category_dict = {}
    for category in category_counter:
        if category in category_list:
            category_dict[category] = category_counter[category]
    return category_dict
