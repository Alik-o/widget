from unittest.mock import patch

from src.external_api import get_currency_conversion


@patch("requests.get")
def test_get_currency_conversion(mock_get):
    mock_get.return_value.json.return_value = {"result": 100}
    assert get_currency_conversion("USD", 20, "2022-02-20") == 100
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=20&date=2022-02-20",
        headers={"apikey": "eMqnueDe0RmQSJN7ctIdLfg6y2Dohj0l"},
        data={},
    )
