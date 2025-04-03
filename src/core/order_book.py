from .utils import OrderSide, OrderType
import heapq

class OrderBook:
    def __init__(self):
        self.bids = [] # max heap for bids
        self.asks = [] # min heap for asks
        self.orders = {} # dictionary to store orders by id

    def add_order(self, order):
        self.orders[order.id] = order
        if order.side == OrderSide.BUY:
            heapq.heappush(self.bids, order)
        else:
            heapq.heappush(self.asks, order)
        self.orders[order.id] = order
    
    def cancel_order(self, order_id: str):
        if order_id in self.orders:
            order = self.orders[order_id]
            if order.side == OrderSide.BUY:
                self.bids.remove(order)
                heapq.heapify(self.bids)
            else:
                self.asks.remove(order)
                heapq.heapify(self.asks)
            del self.orders[order_id]
    
    def get_best_bid(self, side: OrderSide):
        if side == OrderSide.BUY and self.bids:
            return self.bids[0]
        elif side == OrderSide.SELL and self.asks:
            return self.asks[0]
        return None