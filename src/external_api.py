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
    data = response.json()
    amount_rub = round(data["result"], 2)
    return amount_rub
