# commands/add.py
from server.commands.base import Command
from server.exchange import Exchange
from server.order import Order


class AddCommand(Command):
    def __init__(self, order: Order):
        self.order = order

    def run(self, ticker: str) -> dict:
        exchange = Exchange()
        engine = exchange.get_engine(ticker)
        trades = engine.place_order(self.order)

        filled_quantity = sum(t.quantity for t in trades)
        status = (
            "2" if filled_quantity == self.order.quantity else "1" if trades else "0"
        )

        return {
            "message_type": "place_order",
            "order_id": self.order.id,
            "ticker": ticker,
            "quantity": self.order.quantity,
            "side": self.order.side.name,
            "order_type": self.order.order_type.name,
            "order_status": status,
            "trades": [t.to_dict() for t in trades],
        }
