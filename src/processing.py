def filter_by_state(transaction_data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Возвращает отфильтрованный список словарей по ключу"""
    filter_tratransaction_data = []
    for tratransaction in transaction_data:
        if tratransaction["state"] == state:
            filter_tratransaction_data.append(tratransaction)
    return filter_tratransaction_data


def sort_by_date(transaction_data: list[dict], revers: bool=True) -> list[dict]:
    sort_transaction_data = sorted(transaction_data, key=lambda date: date['date'], reverse=revers)
    return sort_transaction_data


if __name__ == "__main__":
    list_transaction_data = [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
    print(filter_by_state(list_transaction_data))

    print(sort_by_date(list_transaction_data))
