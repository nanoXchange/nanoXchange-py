from datetime import datetime, timedelta
import pytest
from server.limit_order import LimitOrder
from server.market_order import MarketOrder
from server.utils import OrderSide, OrderType


def test_limit_order_valid():
    order = LimitOrder(OrderSide.BUY, 10, 101.5)
    assert order.side == OrderSide.BUY
    assert order.quantity == 10
    assert order.price == 101.5
    assert order.order_type == OrderType.LIMIT
    assert order.id.startswith("O")


def test_market_order_valid():
    order = MarketOrder(OrderSide.SELL, 5)
    assert order.side == OrderSide.SELL
    assert order.quantity == 5
    assert order.price is None
    assert order.order_type == OrderType.MARKET


def test_limit_order_invalid_price():
    with pytest.raises(ValueError):
        LimitOrder(OrderSide.BUY, 10, -5)


def test_order_comparison_by_price_and_time():
    o1 = LimitOrder(OrderSide.BUY, 5, 100.0)
    o2 = LimitOrder(OrderSide.BUY, 5, 101.0)
    assert o2 < o1


def test_market_order_timestamp_priority():
    o1 = MarketOrder(OrderSide.SELL, 3)
    o2 = MarketOrder(OrderSide.SELL, 3)
    o1.timestamp = datetime.now()
    o2.timestamp = o1.timestamp + timedelta(seconds=2)
    assert o1 < o2


def test_limit_order_from_dict():
    data = {"side": "buy", "order_type": "limit", "quantity": "5", "price": "101.0"}
    order = LimitOrder.from_dict(data)
    assert isinstance(order, LimitOrder)
    assert order.price == 101.0


def test_market_order_from_dict():
    data = {"side": "sell", "order_type": "market", "quantity": "3"}
    order = MarketOrder.from_dict(data)
    assert isinstance(order, MarketOrder)
    assert order.price is None


def test_from_dict_missing_fields():
    with pytest.raises(KeyError):
        LimitOrder.from_dict({"side": "buy", "quantity": "5"})
