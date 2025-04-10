import pytest
from core.parser import Parser


def test_encode():
    parser = Parser()
    data = {"key1": "value1", "key2": "value2"}
    encoded = parser.encode(data)
    assert encoded == "key1=value1|key2=value2"


def test_encode_add_order():
    parser = Parser()
    data = {"type": "ADD", "ticker": "AAPL", "price": 150.0, "quantity": 100}
    fix = parser.encode(data)
    expected_parts = {"type=ADD", "ticker=AAPL", "price=150.0", "quantity=100"}
    assert set(fix.split("|")) == expected_parts


def test_encode_cancel_order():
    parser = Parser()
    data = {"type": "CANCEL", "order_id": "12345"}
    fix = parser.encode(data)
    expected_parts = {"type=CANCEL", "order_id=12345"}
    assert set(fix.split("|")) == expected_parts


def test_decode_fix_message():
    parser = Parser()
    fix_msg = "56='D'|11='limit'|39='AAPL'|44='150.0'|38='100'|54='1'"
    decoded = parser.decode(fix_msg)
    expected = {
        "message_type": "D",
        "order_type": "limit",
        "ticker": "AAPL",
        "price": "150.0",
        "quantity": "100",
        "side": "1",
    }
    assert decoded == expected


def test_decode_invalid_fix_message():
    parser = Parser()
    invalid_msg = "type=ADD|ticker=AAPL|price=150.0|quantity"
    with pytest.raises(ValueError):
        parser.decode(invalid_msg)


def test_decode_and_encode_round_trip_consistency():
    parser = Parser()
    original = {
        "56": "D",
        "11": "limit",
        "39": "TSLA",
        "44": 800.0,
        "38": 10,
        "54": "1",
    }
    fix_msg = parser.encode(original)
    decoded = parser.decode(fix_msg)
    expected_keys = {
        "message_type",
        "order_type",
        "ticker",
        "price",
        "quantity",
        "side",
    }
    assert expected_keys.issubset(set(decoded.keys()))
