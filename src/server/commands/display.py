# commands/display.py
from server.commands.base import Command
from server.exchange import Exchange


class DisplayCommand(Command):
    def run(self, ticker: str) -> dict:
        exchange = Exchange()
        book = exchange.get_book(ticker)

        return {
            "message_type": "display",  # Display
            "ticker": ticker,
            "bids": [str(o) for o in book.bids],
            "asks": [str(o) for o in book.asks],
            "market_buys": [str(o) for o in book.market_buys],
            "market_sells": [str(o) for o in book.market_sells],
        }
