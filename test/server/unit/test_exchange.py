from server.exchange import Exchange
from server.commands.add import AddCommand
from server.commands.cancel import CancelCommand
from server.commands.display import DisplayCommand
from server.limit_order import LimitOrder
from server.market_order import MarketOrder
from server.utils import OrderSide


def test_add_limit_order_to_exchange():
    exchange = Exchange()
    ticker = "AAPL"
    exchange.add_ticker(ticker)
    order = LimitOrder(OrderSide.BUY, 10, 101.5)
    cmd = AddCommand(order)
    response = cmd.run(ticker)

    assert response["message_type"] == "place_order"
    assert response["order_id"] == order.id
    assert response["ticker"] == ticker
    assert response["quantity"] == 10
    assert response["side"] == "BUY"
    assert response["order_type"] == "LIMIT"
    assert response["order_status"] in ["0", "1", "2"]


def test_add_market_order_to_exchange():
    exchange = Exchange()
    ticker = "GOOG"
    exchange.add_ticker(ticker)
    order = MarketOrder(OrderSide.SELL, 5)
    cmd = AddCommand(order)
    response = cmd.run(ticker)

    assert response["message_type"] == "place_order"
    assert response["order_id"] == order.id
    assert response["ticker"] == ticker
    assert response["quantity"] == 5
    assert response["side"] == "SELL"
    assert response["order_type"] == "MARKET"
    assert response["order_status"] in ["0", "1", "2"]


def test_cancel_existing_order():
    exchange = Exchange()
    ticker = "TSLA"
    exchange.add_ticker(ticker)
    order = LimitOrder(OrderSide.SELL, 20, 420.69)
    exchange.match_engines[ticker].place_order(order)

    cmd = CancelCommand(order.id)
    response = cmd.run(ticker)

    assert response["message_type"] == "cancel_order"
    assert response["order_id"] == order.id
    assert response["ticker"] == ticker
    assert response["order_status"] == "canceled"


def test_cancel_nonexistent_order():
    exchange = Exchange()
    ticker = "TSLA"
    exchange.add_ticker(ticker)

    cmd = CancelCommand("O999999")
    response = cmd.run(ticker)

    assert response["message_type"] == "cancel_order"
    assert response["order_id"] == "O999999"
    assert response["ticker"] == ticker
    assert response["order_status"] == "rejected"


def test_display_command_response_structure():
    exchange = Exchange()
    ticker = "META"
    exchange.add_ticker(ticker)

    cmd = DisplayCommand()
    response = cmd.run(ticker)

    assert response["message_type"] == "display"
    assert response["ticker"] == ticker
    assert "bids" in response
    assert "asks" in response
    assert "market_buys" in response
    assert "market_sells" in response
