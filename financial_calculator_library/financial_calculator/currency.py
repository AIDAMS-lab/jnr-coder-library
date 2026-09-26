"""Simple currency conversion using user-supplied exchange rates.

Rates are stored relative to GHS by default.
For example, USD: 0.067 means 1 GHS = 0.067 USD.
"""

from .utils import validate_positive, round_money

EXCHANGE_RATES = {
    "GHS": 1.0,
    "USD": 0.067,
    "EUR": 0.057,
    "GBP": 0.050,
    "NGN": 103.0,
}


def get_supported_currencies():
    """Return supported currency codes."""
    return sorted(EXCHANGE_RATES.keys())


def set_exchange_rate(currency, rate):
    """Add or update a currency rate relative to GHS."""
    currency = currency.upper()
    validate_positive(rate, "rate")
    EXCHANGE_RATES[currency] = float(rate)


def convert_currency(amount, from_currency, to_currency):
    """Convert money using the stored exchange rates."""
    amount = validate_positive(amount, "amount")
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in EXCHANGE_RATES:
        raise ValueError(f"Unsupported currency: {from_currency}")
    if to_currency not in EXCHANGE_RATES:
        raise ValueError(f"Unsupported currency: {to_currency}")

    # First convert to GHS, then convert to the target currency.
    amount_in_ghs = amount / EXCHANGE_RATES[from_currency]
    result = amount_in_ghs * EXCHANGE_RATES[to_currency]
    return round_money(result)
