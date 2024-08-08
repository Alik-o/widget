import logging
import os
from config import LOG_DIR

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s = %(message)s",
    filename=os.path.join(LOG_DIR, "masks.log"),
    encoding="utf-8",
    filemode="w",
)
mask_card_loger = logging.getLogger("app_card")
mask_account_loger = logging.getLogger("app_account")


def get_mask_card_number(card_number: str) -> str:
    """Возвращает маску карты"""
    mask_card_loger.info("Получены данные карты для маскировки")
    if len(card_number) != 16 or not card_number.isdigit():
        mask_card_loger.warning(f"Данные карты некорректны: {card_number}")
        return "Некорректный номер карты"
    mask_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    mask_card_loger.info("Успешная маскировка карты")

    return mask_card


def get_mask_account(account_number: str) -> str:
    """Возвращает маску счета"""
    mask_account_loger.info("Получены данные счета для маскировки")
    if len(account_number) != 20 or not account_number.isdigit():
        mask_account_loger.warning(f"Данные счета некорректны: {account_number}")
        return "Некорректный номер счета"
    mask_account = f"**{account_number[-4:]}"
    mask_account_loger.info("Успешная маскировка счета")
    return mask_account
