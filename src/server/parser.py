from server.commands.add import AddCommand
from server.commands.base import Command
from server.commands.cancel import CancelCommand
from server.commands.display import DisplayCommand
from .utils import TAG_MAPPINGS, MESSAGE_TYPES
from .order import Order


class Parser:
    """
    A class to parse the input data and convert it into a structured format.
    Encodes and decodes FIX-style messages.
    """

    def __init__(self):
        self.delimiter = "|"
        self.reverse_tag_map = {
            v: k for k, v in TAG_MAPPINGS.items()
        }  # e.g. 'order_type' -> 11

    def encode(self, data: dict) -> str:
        """
        Encodes a dictionary into a FIX-style message.
        Converts human-readable keys to FIX tag numbers and message types back to codes.
        """
        parts = []
        for key, value in data.items():
            if key == "message_type":
                # Reverse lookup to FIX message type code
                fix_code = next(
                    (k for k, v in MESSAGE_TYPES.items() if v == value), value
                )
                parts.append(f"35={fix_code}")
            elif key in self.reverse_tag_map:
                tag = self.reverse_tag_map[key]
                parts.append(f"{tag}={value}")
            elif isinstance(value, list):
                # For lists like trades
                parts.append(f"{key}={value}")
            else:
                parts.append(f"{key}={value}")
        return self.delimiter.join(parts)

    def decode(self, message: str) -> dict:
        """
        Decodes a FIX-style message into a dictionary.
        Maps FIX tags to human-readable keys.
        """
        parts = message.split(self.delimiter)
        data = {}

        for part in parts:
            if "=" not in part:
                raise ValueError(f"Malformed part in message: '{part}'")
            key, value = part.split("=", maxsplit=1)
            value = value.strip().strip("'")

            try:
                tag = int(key.strip())
                if tag in TAG_MAPPINGS:
                    field_name = TAG_MAPPINGS[tag]
                    data[field_name] = value
            except ValueError:
                # Non-numeric keys like 'trades' — just store them as-is
                data[key.strip()] = value

        return data

    def parse_order(self, message: str) -> Command:
        """
        Parses a FIX message and returns a Command object.
        """
        data = self.decode(message)
        message_type = data.get("message_type")
        if message_type not in MESSAGE_TYPES:
            raise ValueError(f"Unknown message type: {message_type}")
        command_type = MESSAGE_TYPES[message_type]

        if command_type == "place_order":
            order = Order.from_dict(data)
            return AddCommand(order)
        elif command_type == "cancel_order":
            order_id = data.get("order_id")
            if not order_id:
                raise ValueError("Missing 'order_id' in cancel order data.")
            return CancelCommand(order_id)
        elif command_type == "display":
            return DisplayCommand()
