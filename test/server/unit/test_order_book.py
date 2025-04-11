from datetime import datetime, timedelta
from server.order_book import OrderBook
from server.limit_order import LimitOrder
from server.market_order import MarketOrder
from server.utils import OrderSide


def test_add_limit_order_buy():
    ob = OrderBook()
    order = LimitOrder(OrderSide.BUY, 10, 100.0)
    assert ob.add_order(order)
    assert order in ob.bids


def test_add_limit_order_sell():
    ob = OrderBook()
    order = LimitOrder(OrderSide.SELL, 10, 105.0)
    assert ob.add_order(order)
    assert order in ob.asks


def test_add_market_order():
    ob = OrderBook()
    mb = MarketOrder(OrderSide.BUY, 5)
    ms = MarketOrder(OrderSide.SELL, 5)
    assert ob.add_order(mb)
    assert ob.add_order(ms)
    assert mb in ob.market_buys
    assert ms in ob.market_sells


def test_remove_limit_order():
    ob = OrderBook()
    order = LimitOrder(OrderSide.SELL, 5, 99.0)
    ob.add_order(order)
    assert ob.remove_order(order.id)
    assert order.id not in ob.orders


def test_remove_market_order():
    ob = OrderBook()
    order = MarketOrder(OrderSide.BUY, 3)
    ob.add_order(order)
    assert ob.remove_order(order.id)
    assert order.id not in ob.orders


def test_get_best_limit_order():
    ob = OrderBook()
    a = LimitOrder(OrderSide.BUY, 5, 99.0)
    b = LimitOrder(OrderSide.BUY, 5, 101.0)
    ob.add_order(a)
    ob.add_order(b)
    assert ob.get_best_limit_order(OrderSide.BUY) == b


def test_get_next_market_order():
    ob = OrderBook()
    o1 = MarketOrder(OrderSide.BUY, 5)
    o2 = MarketOrder(OrderSide.BUY, 5)
    o1.timestamp = datetime.now()
    o2.timestamp = o1.timestamp + timedelta(seconds=1)
    ob.add_order(o2)
    ob.add_order(o1)
    assert ob.get_next_market_order(OrderSide.BUY) == o1


def test_reject_duplicate_order():
    ob = OrderBook()
    order = LimitOrder(OrderSide.BUY, 10, 100.0)
    ob.orders[order.id] = order  # Manually insert
    assert not ob.add_order(order)
