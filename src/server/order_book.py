import heapq
from .utils import OrderSide
from .limit_order import LimitOrder
from .market_order import MarketOrder


class OrderBook:
    def __init__(self):
        """
        Initialize the order book with heaps for limit and market orders,
        and an orders dictionary.
        """
        self.bids = []  # Max-heap for limit BUY orders
        self.asks = []  # Min-heap for limit SELL orders
        self.market_buys = []  # Min-heap for market BUY orders
        self.market_sells = []  # Min-heap for market SELL orders
        self.orders = {}  # Dict for order ID lookup

    def add_order(self, order):
        """
        Add an order to the order book.
        :param order: A LimitOrder or MarketOrder
        :return: True if added successfully, False if duplicate
        """
        if order.id in self.orders:
            return False

        self.orders[order.id] = order

        if isinstance(order, LimitOrder):
            if order.side == OrderSide.BUY:
                heapq.heappush(self.bids, order)
            else:
                heapq.heappush(self.asks, order)
        elif isinstance(order, MarketOrder):
            if order.side == OrderSide.BUY:
                heapq.heappush(self.market_buys, order)
            else:
                heapq.heappush(self.market_sells, order)

        return True

    def remove_order(self, order_id: str):
        """
        Remove an order by ID.
        :param order_id: ID of the order to cancel
        :return: True if canceled, False otherwise
        """
        if order_id not in self.orders:
            return False

        order = self.orders[order_id]

        if isinstance(order, LimitOrder):
            heap = self.bids if order.side == OrderSide.BUY else self.asks
        elif isinstance(order, MarketOrder):
            heap = (
                self.market_buys if order.side == OrderSide.BUY else self.market_sells
            )
        else:
            return False

        heap.remove(order)
        heapq.heapify(heap)

        del self.orders[order_id]
        return True

    def get_best_limit_order(self, side: OrderSide):
        """
        Get the best LIMIT order on the given side.
        :param side: OrderSide.BUY or OrderSide.SELL
        :return: Best LimitOrder or None
        """
        if side == OrderSide.BUY and self.bids:
            return self.bids[0]
        elif side == OrderSide.SELL and self.asks:
            return self.asks[0]
        return None

    def get_next_market_order(self, side: OrderSide):
        """
        Get the next MARKET order on the given side.
        :param side: OrderSide.BUY or OrderSide.SELL
        :return: MarketOrder or None
        """
        queue = self.market_buys if side == OrderSide.BUY else self.market_sells
        return queue[0] if queue else None
