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
