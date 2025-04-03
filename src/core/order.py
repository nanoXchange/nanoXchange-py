import time
from .utils import OrderSide


class Order:
    def __init__(self, id, side, price, quantity, order_type):
        self.id = id
        self.side = side
        self.price = price
        self.quantity = quantity
        self.order_type = order_type
        self.timestamp = time.time()

    def __lt__(self, other):
        if self.side == OrderSide.BUY:
            if self.price != other.price:
                return self.price > other.price
        else:
            if self.price != other.price:
                return self.price < other.price

        return self.timestamp < other.timestamp
