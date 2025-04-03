from enum import Enum

class OrderSide(Enum):
    """
    Enum for order side.
    """
    BUY = "BUY"
    SELL = "sell"

class OrderType(Enum):
    """
    Enum for order type.
    """
    LIMIT = "LIMIT"
    MARKET = "MARKET"