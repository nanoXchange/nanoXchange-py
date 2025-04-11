from .order_book import OrderBook
from .match_engine import MatchEngine


class Exchange:

    # Singleton pattern to ensure only one instance of Exchange exists
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.order_books: dict[str, OrderBook] = {}
        self.match_engines: dict[str, MatchEngine] = {}

    def add_ticker(self, ticker: str):
        book = OrderBook()
        self.order_books[ticker] = book
        self.match_engines[ticker] = MatchEngine(book)

    def get_book(self, ticker: str) -> OrderBook:
        return self.order_books[ticker]

    def get_engine(self, ticker: str) -> MatchEngine:
        return self.match_engines[ticker]
