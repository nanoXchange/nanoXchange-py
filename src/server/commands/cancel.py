# commands/cancel.py
from server.commands.base import Command
from server.exchange import Exchange


class CancelCommand(Command):
    def __init__(self, order_id: str):
        self.order_id = order_id

    def run(self, ticker: str) -> dict:
        exchange = Exchange()
        book = exchange.get_book(ticker)
        removed = book.remove_order(self.order_id)
        return {
            "message_type": "cancel_order",
            "order_id": self.order_id,
            "ticker": ticker,
            "order_status": "canceled" if removed else "rejected",
        }
