import re

from utils.currency_conversion import convert_currency
from config.structures import Currency, get_currency_from_amount


def perform_manual_tribute_input(amount, user, month, current_totals_info):
    from_currency = get_currency_from_amount(amount)
    amount = float(re.sub("[^\d\.]", "", amount))
    try: 
        user_currency = Currency._member_map_[current_totals_info[str(user.id)]["Currency"]]
    except KeyError:
        current_totals_info[str(user.id)] = {"Tributes": [], "Currency": "USD"}
        user_currency = Currency.USD
    amount = convert_currency(amount, from_currency, user_currency)
    try:
        current_totals_info[str(user.id)]["Tributes"][month-1] += amount
    except KeyError:
        current_totals_info[str(user.id)]["Tributes"] = [0.]*12
        current_totals_info[str(user.id)]['Tributes'][month-1] = amount
    return current_totals_info