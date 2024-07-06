from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Возвращает маску карты или счета"""
    varieties_card = [
        "Maestro",
        "MasterCard",
        "Visa Classic",
        "Visa Platinum",
        "Visa Gold",
    ]
    if account_info[:4] == "Счет" and account_info[-20:].isdigit():
        account_number = get_mask_account(account_info[5:])
        mask_account = f"{account_info[:4]} {account_number}"
        return mask_account
    elif account_info[:-17] in varieties_card and account_info[-16:].isdigit():
        mask_card_number = get_mask_card_number(account_info[-16:])
        mask_card = f"{account_info[:-16]}{mask_card_number}"
        return mask_card
    return "Некорректные данные"


def get_data(info_date: str) -> str:
    """Возвращает дату"""
    date_list = info_date[:10].split("-")
    if len(date_list) != 3:
        return "Некорректная дата"
    correct_date = ".".join(date_list[::-1])
    return correct_date
