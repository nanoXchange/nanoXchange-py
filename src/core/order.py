from datetime import datetime
from .utils import OrderSide, OrderType


class Order:
    """
    Represents a trading order.
    Attributes:
        id (str): Unique identifier for the order.
        side (OrderSide): Side of the order (BUY or SELL).
        price (float): Price at which the order is placed.
        quantity (int): Quantity of the asset to be traded.
        order_type (OrderType): Type of the order (LIMIT or MARKET).
        timestamp (datetime): Timestamp when the order was created.
    """

    ## Define the __slots__ to optimize memory usage
    # and improve performance.
    # Internally stores attributes like fields in a C struct.
    # __slots__ = ['id', 'side', 'price', 'quantity', 'order_type', 'timestamp']

    def __init__(self, id: str, side: OrderSide, price: float, quantity: int, order_type: OrderType):
        """
        Initialize an order.
        :param id: Unique identifier for the order.
        :param side: Side of the order (BUY or SELL).
        :param price: Price at which the order is placed.
        :param quantity: Quantity of the asset to be traded.
        :param order_type: Type of the order (LIMIT or MARKET).
        """
        if not isinstance(id, str):
            raise TypeError("Order ID must be a string.")
        if not isinstance(side, OrderSide):
            raise TypeError("Order side must be an instance of OrderSide.")
        if not isinstance(price, (int, float)):
            raise TypeError("Order price must be a number.")
        if not isinstance(quantity, int):
            raise TypeError("Order quantity must be an integer.")
        if not isinstance(order_type, OrderType):
            raise TypeError("Order type must be an instance of OrderType.")
        
        self.id: str = id
        self.side: OrderSide = side
        self.price: float = price
        self.quantity: int = quantity
        self.order_type: OrderType = order_type
        self.timestamp: datetime = datetime.now()



    def __lt__(self, other):
        """
        Compare two orders based on their price and timestamp.
        :param other: The other order to compare against.
        :return: True if this order is less than the other order, False otherwise.
        """

        #TODO: Implement a more optimised comparison logic: short circuit eval, reduce nesting.

        if self.side == OrderSide.BUY:
            if self.price != other.price:
                return self.price > other.price
        else:
            if self.price != other.price:
                return self.price < other.price

        return self.timestamp < other.timestamp
