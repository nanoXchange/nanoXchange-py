from datetime import datetime, timedelta
import pytest
from core.order import Order
from core.utils import OrderSide, OrderType


def test_create_valid_order():
    order = Order("order1", OrderSide.BUY, 100.0, 10, OrderType.LIMIT)
    assert order.id == "order1"
    assert order.side == OrderSide.BUY
    assert order.price == 100.0
    assert order.quantity == 10
    assert order.order_type == OrderType.LIMIT
    assert isinstance(order.timestamp, datetime)


def test_order_invalid_id_type():
    with pytest.raises(TypeError):
        Order(123, OrderSide.BUY, 100.0, 10, OrderType.LIMIT)


def test_order_invalid_side_type():
    with pytest.raises(TypeError):
        Order("order2", "BUY", 100.0, 10, OrderType.LIMIT)


def test_order_invalid_price_type():
    with pytest.raises(TypeError):
        Order("order3", OrderSide.BUY, "100", 10, OrderType.LIMIT)


def test_order_invalid_quantity_type():
    with pytest.raises(TypeError):
        Order("order4", OrderSide.BUY, 100.0, "ten", OrderType.LIMIT)


def test_order_invalid_order_type():
    with pytest.raises(TypeError):
        Order("order5", OrderSide.SELL, 100.0, 10, "LIMIT")


def test_order_less_than_comparison_buy():
    order1 = Order("o1", OrderSide.BUY, 100.0, 10, OrderType.LIMIT)
    order2 = Order("o2", OrderSide.BUY, 101.0, 10, OrderType.LIMIT)
    assert order2 < order1  # Higher price first for BUY


def test_order_less_than_comparison_sell():
    order1 = Order("o1", OrderSide.SELL, 100.0, 10, OrderType.LIMIT)
    order2 = Order("o2", OrderSide.SELL, 99.0, 10, OrderType.LIMIT)
    assert order2 < order1  # Lower price first for SELL


def test_order_less_than_same_price_by_timestamp():
    order1 = Order("o1", OrderSide.BUY, 100.0, 10, OrderType.LIMIT)
    order2 = Order("o2", OrderSide.BUY, 100.0, 10, OrderType.LIMIT)
    order1.timestamp = datetime.now()
    order2.timestamp = order1.timestamp + timedelta(seconds=1)
    assert order1 < order2  # Earlier timestamp wins


def test_order_timestamp_is_recent():
    order = Order("order6", OrderSide.SELL, 99.99, 1, OrderType.MARKET)
    now = datetime.now()
    assert now - order.timestamp < timedelta(seconds=1)
