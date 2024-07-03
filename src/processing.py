def filter_by_state(transaction_data: list[dict], state: str = "EXECUTED") -> list:
    """Возвращает отфильтрованный список словарей по ключу"""
    filter_transaction_data = []
    for transaction in transaction_data:
        if transaction.get("state") == state:
            filter_transaction_data.append(transaction)
        elif transaction.get("state"):
            continue
    return filter_transaction_data


def sort_by_date(transaction_data: list[dict], ascending: bool = True) -> list[dict]:
    """Возвращает отсортированный список словарей по дате"""
    sort_transaction_data = sorted(transaction_data, key=lambda date: date["date"], reverse=ascending)
    return sort_transaction_data
