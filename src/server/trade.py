from datetime import datetime


class Trade:
    def __init__(self, buy_id: str, sell_id: str, quantity: int, price: float):
        """
        Represents a trade between two parties.
        :param buy_id: ID of the buyer
        :param sell_id: ID of the seller
        :param quantity: Quantity of the asset traded
        :param price: Price at which the trade occurred
        """
        # TODO: move this out of here, ensure some constraint check on the params before calling init
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        if not isinstance(buy_id, str) or not isinstance(sell_id, str):
            raise ValueError("Buy ID and Sell ID must be strings")
        if not buy_id or not sell_id:
            raise ValueError("Buy ID and Sell ID cannot be empty strings")
        if len(buy_id) > 20 or len(sell_id) > 20:
            raise ValueError("Buy ID and Sell ID cannot exceed 20 characters")

        self.buy_id: str = buy_id
        self.sell_id: str = sell_id
        self.quantity: int = quantity
        self.price: float = price
        self.timestamp: datetime = datetime.now()

    def to_dict(self) -> dict:
        return {
            "buy_id": self.buy_id,
            "sell_id": self.sell_id,
            "quantity": self.quantity,
            "price": self.price,
            "timestamp": self.timestamp.isoformat(),
        }

    def __str__(self):
        def format_quantity(qty):
            if qty >= 1_000_000:
                return f"{qty / 1_000_000:.1f}M"
            elif qty >= 1_000:
                return f"{qty / 1_000:.1f}K"
            else:
                return str(qty)

        return f"{self.timestamp} | {self.buy_id} bought {format_quantity(self.quantity)} at ${self.price:.2f} from {self.sell_id}"
