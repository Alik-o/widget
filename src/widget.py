from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Возвращает маску карты или счета"""
    if account_info[:4] == "Счет":
        account_number = get_mask_account(account_info[5:])
        mask_account = f"{account_info[:4]} {account_number}"
        return mask_account
    else:
        mask_card_number = get_mask_card_number(account_info[-16:])
        mask_card = f"{account_info[:-16]} {mask_card_number}"
        return mask_card


def get_data(info_date: str) -> str:
    """Возвращает дату"""
    date_list = info_date[:10].split("-")
    correct_date = ".".join(date_list[::-1])
    return correct_date


if __name__ == "__main__":
    print(get_data("2018-07-11T02:26:18.671407"))
