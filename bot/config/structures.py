from dataclasses import dataclass
from enum import IntEnum, auto
from typing import *

class Currency(IntEnum):
    USD = auto()
    EUR = auto()
    HUF = auto()

USD = Currency.USD
EUR = Currency.EUR
HUF = Currency.HUF

def get_currency_from_amount(amount: str) -> Currency:
    if "EUR" in amount or "€" in amount:
        return EUR
    elif "HUF" in amount:
        return HUF
    else:
        return USD

@dataclass
class TributeInformation:
    UserID: str
    Amount: float
    Currency: Currency
    Platform: Optional[str]
