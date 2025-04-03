import time
from src.core.order_book import OrderBook
from src.core.utils import OrderSide, OrderType
from src.core.order import Order


def test_add_buy_order():
    order_book = OrderBook()
    order = Order(
        id="1", side=OrderSide.BUY, price=100.0, quantity=10, order_type=OrderType.LIMIT
    )
    order_book.add_order(order)
    assert len(order_book.bids) == 1
    assert order_book.bids[0] == order


def test_add_sell_order():
    order_book = OrderBook()
    order = Order(
        id="2", side=OrderSide.SELL, price=101.0, quantity=5, order_type=OrderType.LIMIT
    )
    order_book.add_order(order)
    assert len(order_book.asks) == 1
    assert order_book.asks[0] == order


def test_cancel_order():
    order_book = OrderBook()
    order = Order(id="3", side=OrderSide.BUY, price=100.0, quantity=10, order_type=OrderType.LIMIT)  # type: ignore
    order_book.add_order(order)
    order_book.cancel_order(order.id)
    assert len(order_book.bids) == 0
    assert order.id not in order_book.orders


def test_get_best_bid():
    order_book = OrderBook()
    order1 = Order(id="4", side=OrderSide.BUY, price=100.0, quantity=10, order_type=OrderType.LIMIT)  # type: ignore
    order2 = Order(id="5", side=OrderSide.BUY, price=101.0, quantity=5, order_type=OrderType.LIMIT)  # type: ignore
    order_book.add_order(order1)
    order_book.add_order(order2)
    best_bid = order_book.get_best_bid(OrderSide.BUY)
    assert best_bid == order2  # highest price should be returned
