from enum import Enum


# TODO: Check if there are memory optimisations for using B/S instead of BUY/SELL
class OrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"


# TODO: Check if there are memory optimisations for using L/M instead of LIMIT/MARKET
class OrderType(Enum):
    LIMIT = "LIMIT"
    MARKET = "MARKET"


TAG_MAPPINGS = {
    11: "order_type",
    38: "quantity",
    39: "ticker",
    44: "price",
    54: "side",
    55: "order_status",
    56: "message_type",
    57: "order_id",
}

MESSAGE_TYPES = {
    "D": "place_order",
    "F": "cancel_order",
    "8": "display",
}

ORDER_STATUS_MAP = {
    "0": "new",
    "1": "partially_filled",
    "2": "filled",
    "4": "canceled",
    "8": "rejected",
}
