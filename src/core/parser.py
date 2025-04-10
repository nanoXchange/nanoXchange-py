from core.commands.add import AddCommand
from core.commands.base import Command
from core.commands.cancel import CancelCommand
from core.commands.display import DisplayCommand
from .utils import TAG_MAPPINGS, MESSAGE_TYPES
from .order import Order


class Parser:
    """
    A class to parse the input data and convert it into a structured format.
    Encodes and decodes FIX-style messages.
    """

    def __init__(self):
        self.delimiter = "|"

    def encode(self, data: dict) -> str:
        """
        Encodes a dictionary into a FIX-style message.
        :param data: Dictionary to encode in key-value format
        :return: Encoded string in FIX format
        """
        parts = [f"{key}={value}" for key, value in data.items()]
        return self.delimiter.join(parts)

    def decode(self, message: str) -> dict:
        """
        Decodes a FIX-style message into a dictionary.
        :param message: Encoded string in FIX format
        :return: Decoded dictionary
        """
        parts = message.split(self.delimiter)
        data = {}
        for part in parts:
            if "=" not in part:
                raise ValueError(f"Malformed part in message: '{part}'")
            key, value = part.split("=")
            tag = int(key.strip())
            value = value.strip().strip("'")

            if tag in TAG_MAPPINGS:
                field_name = TAG_MAPPINGS[tag]
                data[field_name] = value

        return data

    def parse_order(self, message: str) -> Command:
        """
        Parses a FIX message and returns an Command object.
        :param message: Encoded string in FIX format
        :return: Order object
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
