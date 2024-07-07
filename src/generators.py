from typing import Generator


def filter_by_currency(list_transactions: list, transfer_currency: str | None = None) -> Generator:
    """Возвращает список транзакций отфильтрованный по валюте"""
    if transfer_currency is None:
        raise ValueError("Задайте валюту для фильтрации")

    for transaction in list_transactions:
        if transaction["operationAmount"]["currency"].get("name") != transfer_currency:
            continue
        yield transaction


def transaction_descriptions(list_transactions: list) -> Generator:
    """Возвращает описание каждой операции"""
    for transaction in list_transactions:
        description = transaction["description"]
        yield description


def card_number_generator(start: int, end: int) -> Generator:
    """Возвращает номер карты из заданного диапазона"""
    if end > 10**16:
        raise ValueError("Превышен диапазон нумерации карт")
    card_range = range(start, end + 1)
    for card in card_range:
        number_card = str(card)
        while len(number_card) < 16:
            number_card = "0" + number_card
        yield f"{number_card[0:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:]}"
