import time

class Order:
    def __init__(self, id, side, price, quantity, order_type):
        self.id = id
        self.side = side
        self.price = price
        self.quantity = quantity
        self.order_type = order_type
        self.timestamp = time.time()