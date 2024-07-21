import os

import requests
from dotenv import load_dotenv


def get_currency_conversion(currency: str, amount: float, date: str) -> float:
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    headers = {"apikey": API_KEY}
    payload = {}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}&date={date}"
    response = requests.get(url, headers=headers, data=payload)
    status_code = response.status_code
    if status_code == 200:
        data = response.json()
        amount_rub = round(data["result"], 2)
        return amount_rub
    else:
        raise Exception("Ошибка при конвертации")


if __name__ == "__main__":
    get_currency_conversion("USD", 100, "2019-08-26")

    # "2019-08-26"
