def get_mask_card_number(card_number: str) -> str:
    """Возвращает маску карты"""
    if len(card_number) != 16 or not card_number.isdigit():
        return "Некорректный номер карты"
    mask_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return mask_card


def get_mask_account(account_number: str) -> str:
    """Возвращает маску счета"""
    if len(account_number) != 20 or not account_number.isdigit():
        return "Некорректный номер счета"
    mask_account = f"**{account_number[-4:]}"
    return mask_account
