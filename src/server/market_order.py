from .utils import OrderSide, OrderType
from .order import Order
from typing import Optional, Any


class MarketOrder(Order):
    def __init__(self, side: OrderSide, quantity: int):
        super().__init__(side, quantity)

    @property
    def price(self) -> Optional[float]:
        return None

    @property
    def order_type(self) -> OrderType:
        return OrderType.MARKET

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "MarketOrder":
        side = OrderSide[data["side"].upper()]
        quantity = int(data["quantity"])
        return MarketOrder(side=side, quantity=quantity)

    def __lt__(self, other: "Order") -> bool:
        if not isinstance(other, Order):
            return NotImplemented

        if not isinstance(other, MarketOrder):
            return True  # Prioritize Market Order

        if self.timestamp != other.timestamp:
            return self.timestamp < other.timestamp
        return self.get_id < other.get_id

    def __str__(self):
        return f"{self.timestamp} | {self.side.name} {self.quantity} (Market) (id={self.id})"
