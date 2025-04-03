import pytest
from core.trade import Trade


def test_create_valid_trade():
    trade = Trade("buyer1", "seller1", 100, 50.0)
    assert trade.buy_id == "buyer1"
    assert trade.sell_id == "seller1"
    assert trade.quantity == 100
    assert trade.price == 50.0
    assert trade.timestamp is not None


def test_trade_quantity_must_be_int():
    with pytest.raises(ValueError):
        Trade("buyer1", "seller1", 100.5, 50.0)


def test_trade_quantity_must_be_positive():
    with pytest.raises(ValueError):
        Trade("buyer1", "seller1", 0, 50.0)


def test_trade_price_must_be_positive():
    with pytest.raises(ValueError):
        Trade("buyer1", "seller1", 10, 0)


def test_trade_ids_must_be_strings():
    with pytest.raises(ValueError):
        Trade(1, 2, 100, 50.0)


def test_trade_ids_must_not_be_empty():
    with pytest.raises(ValueError):
        Trade("", "", 100, 50.0)


def test_trade_ids_length_limit():
    long_id = "a" * 21
    with pytest.raises(ValueError):
        Trade(long_id, "seller", 10, 5.0)


def test_trade_str_format_small_qty():
    trade = Trade("buyer", "seller", 999, 45.678)
    s = str(trade)
    assert "999" in s
    assert "$45.68" in s


def test_trade_str_format_large_qty_k():
    trade = Trade("buyer", "seller", 12_000, 23.4)
    s = str(trade)
    assert "12.0K" in s


def test_trade_str_format_large_qty_m():
    trade = Trade("buyer", "seller", 1_500_000, 10.0)
    s = str(trade)
    assert "1.5M" in s
