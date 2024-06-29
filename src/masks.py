def get_mask_card_number(card_number: str) -> str:
    """Возвращает маску карты"""
    mask_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return mask_card


def get_mask_account(account_number: str) -> str:
    """Возвращает маску счета"""
    mask_account = f"**{account_number[-4:]}"
    return mask_account


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print((get_mask_account("73654108430135874305")))
