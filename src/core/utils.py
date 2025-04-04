from enum import Enum


# TODO: Check if there are memory optimisations for using B/S instead of BUY/SELL
class OrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"


# TODO: Check if there are memory optimisations for using L/M instead of LIMIT/MARKET
class OrderType(Enum):
    LIMIT = "LIMIT"
    MARKET = "MARKET"
