import re

from utils.currency_conversion import convert_currency
from config.structures import Currency, get_currency_from_amount



def perform_manual_tribute_input(amount, user, current_totals_info):
    from_currency = get_currency_from_amount(amount)
    amount = float(re.sub("[^\d\.]", "", amount))
    amount = convert_currency(amount, from_currency, Currency.USD)
    try:
        current_totals_info[str(user.id)] += amount
    except KeyError:
        current_totals_info[str(user.id)] = amount
    return current_totals_info