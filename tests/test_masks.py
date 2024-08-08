import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card, mask_card",
    [
        ("7158300734726758", "7158 30** **** 6758"),
        ("1596837868705199", "1596 83** **** 5199"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_get_mask_card_number(card, mask_card):
    assert get_mask_card_number(card) == mask_card


def test_get_mask_card_number_incorrect():
    assert get_mask_card_number("22536565a9883121") == "Некорректный номер карты"


def test_get_mask_card_number_empty_card(no_data):
    assert get_mask_card_number(no_data) == "Некорректный номер карты"


def test_test_get_mask_card_number_less(less_required_amount):
    assert get_mask_card_number(less_required_amount) == "Некорректный номер карты"


def test_test_get_mask_card_number_more(more_required_amount):
    assert get_mask_card_number(more_required_amount) == "Некорректный номер карты"


@pytest.mark.parametrize(
    "bank_account, mask_bank_account",
    [("73654108430135874305", "**4305"), ("35383033474447895560", "**5560"), ("64686473678894779589", "**9589")],
)
def test_get_mask_account(bank_account, mask_bank_account):
    assert get_mask_account(bank_account) == mask_bank_account


def test_get_mask_account_empty_account(no_data):
    assert get_mask_account(no_data) == "Некорректный номер счета"


def test_get_mask_account_less(less_required_amount):
    assert get_mask_account(less_required_amount) == "Некорректный номер счета"


def test_get_mask_account_more(more_required_amount):
    assert get_mask_account(more_required_amount) == "Некорректный номер счета"


def test_get_mask_account_incorrect():
    assert get_mask_account("c4686473678894779589") == "Некорректный номер счета"
