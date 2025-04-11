from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Optional
from .utils import OrderSide, OrderType


class Order(ABC):
    _id_counter: int = 1

    def __init__(
        self,
        side: OrderSide,
        quantity: int,
    ):
        if not isinstance(side, OrderSide):
            raise TypeError("Order side must be OrderSide.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise TypeError("Quantity must be a positive integer.")

        self.id: str = self._generate_id()
        self.side: OrderSide = side
        self.quantity: int = quantity
        self.timestamp: datetime = datetime.now()

    @classmethod
    def _generate_id(cls) -> str:
        id_str = f"O{cls._id_counter}"
        cls._id_counter += 1
        return id_str

    @property
    def get_id(self) -> str:
        return self.id

    @property
    @abstractmethod
    def order_type(self) -> OrderType: ...

    @property
    @abstractmethod
    def price(self) -> Optional[float]: ...

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Order":
        order_type = data.get("order_type", "").upper()

        if order_type == "LIMIT":
            from server.limit_order import LimitOrder  # defer import

            return LimitOrder.from_dict(data)
        elif order_type == "MARKET":
            from server.market_order import MarketOrder  # defer import

            return MarketOrder.from_dict(data)
        else:
            raise ValueError(f"Unsupported order_type: {order_type}")

    @abstractmethod
    def __lt__(self, other: "Order") -> bool:
        raise NotImplementedError(
            "Subclasses of Order should implement __lt__ comparison"
        )

    def __str__(self):
        return f"{self.timestamp} | {self.side.name} {self.quantity} @ {self.price} (id={self.id})"
