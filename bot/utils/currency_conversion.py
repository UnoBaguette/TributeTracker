import requests

from config.structures import Currency

API_REQUEST_URL = "https://v6.exchangerate-api.com/v6/004ab474335448d1d88960ec/latest/"

def convert_currency(amount: float, from_currency: Currency, to_currency: Currency) -> float:
    if from_currency == to_currency: return amount
    try:
        response = requests.get(f"{API_REQUEST_URL}{from_currency.name.upper()}")
        data = response.json()
        rate = data['conversion_rates'][to_currency.name.upper()]
        return amount * rate
    except Exception as e:
        print(f"API error: {e}")
        return None