from utils import OrderSide
import heapq


class OrderBook:
    def __init__(self):
        self.bids = []  # List of bid orders
        self.asks = []  # List of ask orders
        self.orders = {}  # Dictionary to store orders by ID

    def add_order(self, order: Order): # type: ignore
        """
        Add an order to the order book.
        :param order: Order object to be added
        """
        self.orders[order.order_id] = order
        if order.side == OrderSide.BUY:
            heapq.heappush(self.bids, order)
        else:
            heapq.heappush(self.asks, order)
        self.orders[order.order_id] = order
    
    def cancel_order(self, order_id: str):
        """
        Cancel an order by its ID.
        :param order_id: ID of the order to be canceled
        """
        if order_id in self.orders:
            order = self.orders[order_id]
            if order.side == OrderSide.BUY:
                self.bids.remove(order)
                heapq.heapify(self.bids)
            else:
                self.asks.remove(order)
                heapq.heapify(self.asks)
            del self.orders[order_id]
    
    def get_best(self, side: OrderSide):
        """
        Get the best order from the order book.
        :param side: Order side (BUY or SELL)
        :return: Best order object
        """
        if side == OrderSide.BUY:
            return self.bids[0] if self.bids else None
        else:
            return self.asks[0] if self.asks else None

