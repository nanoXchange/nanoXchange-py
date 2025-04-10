import pytest
from server.parser import Parser


@pytest.fixture
def parser():
    return Parser()


def test_basic_encode(parser):
    data = {"message_type": "place_order", "ticker": "AAPL", "price": 150.0}
    encoded = parser.encode(data)
    assert "35=D" in encoded
    assert "39=AAPL" in encoded
    assert "44=150.0" in encoded


def test_basic_decode(parser):
    message = "35=D|11=LIMIT|38=100|39=TSLA|44=700.0|54=BUY"
    decoded = parser.decode(message)
    assert decoded == {
        "message_type": "D",
        "order_type": "LIMIT",
        "quantity": "100",
        "ticker": "TSLA",
        "price": "700.0",
        "side": "BUY",
    }


def test_encode_with_list(parser):
    data = {
        "message_type": "place_order",
        "order_id": "O123",
        "ticker": "AAPL",
        "quantity": 10,
        "side": "BUY",
        "order_type": "LIMIT",
        "order_status": "0",
        "trades": [{"buy_id": "O1", "sell_id": "O2", "quantity": 5, "price": 150.0}],
    }
    encoded = parser.encode(data)
    assert "35=D" in encoded
    assert "trades=" in encoded
    assert "57=O123" in encoded


def test_round_trip_encode_decode(parser):
    original = {
        "message_type": "D",
        "order_type": "MARKET",
        "ticker": "GOOG",
        "quantity": "15",
        "side": "SELL",
    }
    encoded = parser.encode(original)
    decoded = parser.decode(encoded)
    assert decoded["message_type"] == "D"
    assert decoded["ticker"] == "GOOG"
    assert decoded["order_type"] == "MARKET"
    assert decoded["quantity"] == "15"
    assert decoded["side"] == "SELL"


def test_invalid_message_missing_equal_sign(parser):
    msg = "35D|11=LIMIT|38=10"
    with pytest.raises(ValueError):
        parser.decode(msg)


def test_display_command_encode(parser):
    data = {
        "message_type": "display",
        "ticker": "MSFT",
        "bids": ["buy1", "buy2"],
        "asks": ["sell1"],
        "market_buys": [],
        "market_sells": [],
    }
    encoded = parser.encode(data)
    assert "35=8" in encoded
    assert "39=MSFT" in encoded
    assert "bids=['buy1', 'buy2']" in encoded


def test_cancel_order_encode(parser):
    data = {
        "message_type": "cancel_order",
        "order_id": "O9999",
        "ticker": "TSLA",
        "order_status": "rejected",
    }
    encoded = parser.encode(data)
    assert "35=F" in encoded
    assert "57=O9999" in encoded
    assert "55=rejected" in encoded


def test_decode_realistic_trade_message(parser):
    msg = (
        "35=D|57=O1|39=AAPL|38=0|54=BUY|11=MARKET|55=1|"
        "trades=[{'buy_id': 'O1', 'sell_id': 'O6', 'quantity': 5, 'price': 150.0}]"
    )
    decoded = parser.decode(msg)
    assert decoded["message_type"] == "D"
    assert decoded["order_id"] == "O1"
    assert decoded["ticker"] == "AAPL"
    assert decoded["order_type"] == "MARKET"
    assert "trades" in decoded


def test_decode_invalid_tag(parser):
    msg = "999=abc|38=10|35=D"
    decoded = parser.decode(msg)
    # Tag 999 should be ignored since it's not in TAG_MAPPINGS
    assert "quantity" in decoded
    assert "message_type" in decoded
    assert "order_type" not in decoded
