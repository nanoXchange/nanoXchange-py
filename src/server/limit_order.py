from .utils import OrderSide, OrderType
from .order import Order
from .market_order import MarketOrder
from typing import Any


class LimitOrder(Order):
    def __init__(
        self,
        side: OrderSide,
        quantity: int,
        price: float,
    ):
        if not isinstance(price, (int, float)) or price <= 0:
            raise TypeError("Price must be a positive number.")
        self._price = float(price)
        super().__init__(side, quantity)

    @property
    def price(self) -> float:
        return self._price

    @property
    def order_type(self) -> OrderType:
        return OrderType.LIMIT

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "LimitOrder":
        side = OrderSide[data["side"].upper()]
        quantity = int(data["quantity"])
        price = float(data["price"])
        return LimitOrder(side=side, quantity=quantity, price=price)

    def __lt__(self, other: "Order") -> bool:
        if not isinstance(other, Order):
            return NotImplemented

        if isinstance(other, MarketOrder):
            return False  # Prioritise Market Order

        if self.side == OrderSide.BUY:
            if self.price != other.price:
                return self.price > other.price
        else:
            if self.price != other.price:
                return self.price < other.price

        if self.timestamp != other.timestamp:
            return self.timestamp < other.timestamp
        return self.get_id < other.get_id
