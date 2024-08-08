import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "numbers_account_card, mask",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_account_card(numbers_account_card, mask):
    assert mask_account_card(numbers_account_card) == mask


def test_mask_account_card_empty(no_data):
    assert mask_account_card(no_data) == "Некорректные данные"


@pytest.mark.parametrize(
    "info_date, correct_date",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
    ],
)
def test_get_data(info_date, correct_date):
    assert get_data(info_date) == correct_date


def test_get_data_empty(no_data):
    assert get_data(no_data) == "Некорректная дата"
