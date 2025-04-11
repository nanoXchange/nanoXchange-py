import pytest
from server.order_book import OrderBook
from server.match_engine import MatchEngine
from server.limit_order import LimitOrder
from server.market_order import MarketOrder
from server.utils import OrderSide


def test_engine_initializes_with_book():
    ob = OrderBook()
    engine = MatchEngine(ob)
    assert engine.book == ob
    assert engine.trades == []


def test_execute_trade_basic():
    ob = OrderBook()
    engine = MatchEngine(ob)

    taker = LimitOrder(OrderSide.BUY, 10, 100.0)
    maker = LimitOrder(OrderSide.SELL, 5, 99.0)
    ob.add_order(maker)

    trade = engine.execute_trade(taker, maker)

    assert trade.quantity == 5
    assert trade.price == 99.0
    assert taker.quantity == 5
    assert maker.quantity == 0
    assert trade.buy_id == taker.id
    assert trade.sell_id == maker.id
    assert trade in engine.trades


def test_limit_order_fully_matches_and_removes():
    ob = OrderBook()
    engine = MatchEngine(ob)

    sell = LimitOrder(OrderSide.SELL, 5, 100.0)
    ob.add_order(sell)

    buy = LimitOrder(OrderSide.BUY, 5, 101.0)
    trades = engine.place_order(buy)

    assert len(trades) == 1
    assert ob.get_best_limit_order(OrderSide.SELL) is None


def test_limit_order_partially_matches_and_queues_remainder():
    ob = OrderBook()
    engine = MatchEngine(ob)

    sell = LimitOrder(OrderSide.SELL, 3, 100.0)
    ob.add_order(sell)

    buy = LimitOrder(OrderSide.BUY, 5, 101.0)
    trades = engine.place_order(buy)

    assert len(trades) == 1
    assert trades[0].quantity == 3
    assert buy.quantity == 2
    assert buy.id in ob.orders


def test_limit_order_price_mismatch_no_match():
    ob = OrderBook()
    engine = MatchEngine(ob)

    sell = LimitOrder(OrderSide.SELL, 5, 105.0)
    ob.add_order(sell)

    buy = LimitOrder(OrderSide.BUY, 5, 100.0)
    trades = engine.place_order(buy)

    assert len(trades) == 0
    assert buy.id in ob.orders
    assert sell.id in ob.orders


def test_market_order_fully_consumes_book():
    ob = OrderBook()
    engine = MatchEngine(ob)

    ob.add_order(LimitOrder(OrderSide.SELL, 5, 99.0))

    market_buy = MarketOrder(OrderSide.BUY, 5)
    trades = engine.place_order(market_buy)

    assert len(trades) == 1
    assert trades[0].price == 99.0
    assert trades[0].quantity == 5
    assert market_buy.quantity == 0


def test_market_order_partial_fill_and_queue():
    ob = OrderBook()
    engine = MatchEngine(ob)

    ob.add_order(LimitOrder(OrderSide.SELL, 3, 100.0))

    market_buy = MarketOrder(OrderSide.BUY, 6)
    trades = engine.place_order(market_buy)

    assert len(trades) == 1
    assert trades[0].quantity == 3
    assert market_buy.quantity == 3
    assert market_buy.id in ob.orders


def test_market_order_no_liquidity():
    ob = OrderBook()
    engine = MatchEngine(ob)

    market_sell = MarketOrder(OrderSide.SELL, 5)
    trades = engine.place_order(market_sell)

    assert len(trades) == 0
    assert market_sell.id in ob.orders


def test_invalid_order_type_raises():
    ob = OrderBook()
    engine = MatchEngine(ob)

    with pytest.raises(TypeError):
        engine.place_order("this is not an order")
