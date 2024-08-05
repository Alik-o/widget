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


# if __name__ == '__main__':
#     import os
#     from config import DATA_DIR
#     from src.utils import get_financial_transaction_data
#
#     s = get_financial_transaction_data(os.path.join(DATA_DIR, 'transactions.csv'))
#     p = search_by_description(s, 'открытие')
#     print(p)
#     for transaction in p:
#         print(f"{transaction['date']} {transaction['description']}")
#         if transaction["from"]:
#             print(f'{transaction["from"]} -> {transaction["to"]}')
#         else:
#             print(f'{transaction["to"]}')
#
#
