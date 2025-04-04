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
            if '=' not in part:
                raise ValueError(f"Malformed part in message: '{part}'")
            key, value = part.split("=")
            data[key] = value
        return data
