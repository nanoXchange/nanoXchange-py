from .order_book import OrderBook
from .utils import OrderSide
from .limit_order import LimitOrder
from .market_order import MarketOrder
from .trade import Trade
from typing import Union


class MatchEngine:
    def __init__(self, book: OrderBook):
        """
        Initialize the MatchEngine with an OrderBook instance.
        """
        if not isinstance(book, OrderBook):
            raise TypeError("MatchEngine requires an OrderBook instance.")
        self.book = book
        self.trades: list[Trade] = []

    def get_opposite_side(self, order) -> OrderSide:
        return OrderSide.BUY if order.side == OrderSide.SELL else OrderSide.SELL

    def execute_trade(self, taker, maker) -> Trade:
        """
        Execute a trade between a taker (incoming order) and a maker (existing order).
        """
        quantity = min(taker.quantity, maker.quantity)
        price = maker.price  # Always use maker's price

        trade = Trade(
            buy_id=taker.id if taker.side == OrderSide.BUY else maker.id,
            sell_id=taker.id if taker.side == OrderSide.SELL else maker.id,
            quantity=quantity,
            price=price,
        )

        self.trades.append(trade)

        taker.quantity -= quantity
        maker.quantity -= quantity

        if maker.quantity == 0:
            self.book.remove_order(maker.id)

        return trade

    def match_market_order(self, order: MarketOrder) -> list[Trade]:
        trades = []
        best = self.book.get_best_limit_order(self.get_opposite_side(order))

        while best and order.quantity > 0:
            trades.append(self.execute_trade(order, best))
            best = self.book.get_best_limit_order(self.get_opposite_side(order))

        if order.quantity > 0:
            # Queue remaining unmatched market order
            self.book.add_order(order)

        return trades

    def match_limit_order(self, order: LimitOrder) -> list[Trade]:
        trades = []
        best = self.book.get_best_limit_order(self.get_opposite_side(order))

        while best and order.quantity > 0:
            if order.side == OrderSide.BUY and order.price >= best.price:
                trades.append(self.execute_trade(order, best))
            elif order.side == OrderSide.SELL and order.price <= best.price:
                trades.append(self.execute_trade(order, best))
            else:
                break
            best = self.book.get_best_limit_order(self.get_opposite_side(order))

        if order.quantity > 0:
            self.book.add_order(order)

        return trades

    def place_order(self, order: Union[LimitOrder, MarketOrder]) -> list[Trade]:
        if isinstance(order, MarketOrder):
            return self.match_market_order(order)
        elif isinstance(order, LimitOrder):
            return self.match_limit_order(order)
        else:
            raise TypeError("Unsupported order type")
