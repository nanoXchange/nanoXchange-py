from .utils import OrderSide
import heapq


class OrderBook:
    def __init__(self):
        """
        Initialize the order book with empty bids and asks heaps and an orders dictionary.
        Attributes:
            bids (list): Max heap for buy orders.
            asks (list): Min heap for sell orders.
            orders (dict): Dictionary to store orders by id.
        """
        self.bids = []  # max heap for bids
        self.asks = []  # min heap for asks
        self.orders = {}  # dictionary to store orders by id

    def add_order(self, order):
        """
        Add an order to the order book.
        :param order: The order to be added.
        Returns:
        bool: True if the order was added successfully, False otherwise.
        """
        if order.id in self.orders:
            return False
        self.orders[order.id] = order
        if order.side == OrderSide.BUY:
            heapq.heappush(self.bids, order)
        else:
            heapq.heappush(self.asks, order)
        self.orders[order.id] = order

    def cancel_order(self, order_id: str):
        """
        Cancel an order by its ID.
        :param order_id: The ID of the order to be canceled.
        Returns:
        bool: True if the order was canceled successfully, False otherwise.
        """
        if order_id not in self.orders:
            return False

        order = self.orders[order_id]
        if order.side == OrderSide.BUY:
            self.bids.remove(order)
            heapq.heapify(self.bids)
        else:
            self.asks.remove(order)
            heapq.heapify(self.asks)
        del self.orders[order_id]

    def get_best_bid(self, side: OrderSide):
        """
        Get the best bid or ask from the order book.
        :param side: The side of the order (BUY or SELL).
        Returns:
        Order: The best order from the order book.
        """
        if side == OrderSide.BUY and self.bids:
            return self.bids[0]
        elif side == OrderSide.SELL and self.asks:
            return self.asks[0]
        return None
