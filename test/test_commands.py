from core.order import Order
from core.utils import OrderSide, OrderType
from core.commands.add import AddCommand
from core.commands.cancel import CancelCommand
from core.commands.display import DisplayCommand


def test_add_command_structure():
    order = Order(None, OrderSide.BUY, 100.0, 10, OrderType.LIMIT)
    command = AddCommand(order)

    assert isinstance(command, AddCommand)
    assert hasattr(command, "run")
    assert command.order == order


def test_cancel_command_structure():
    command = CancelCommand(order_id="ORD-001")

    assert isinstance(command, CancelCommand)
    assert hasattr(command, "run")
    assert command.order_id == "ORD-001"


def test_display_command_structure():
    command = DisplayCommand()

    assert isinstance(command, DisplayCommand)
    assert hasattr(command, "run")
