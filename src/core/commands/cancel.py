from .base import Command


class CancelCommand(Command):
    def __init__(self, order_id: str):
        """
        Initialize the CancelCommand with an order ID.
        :param order_id: The ID of the order to be canceled.
        """
        self.order_id = order_id

    def run(self, exchange):
        """
        Execute the command to cancel an order on the exchange.
        :param exchange: The exchange on which the order will be canceled.
        """
        raise NotImplementedError("Exchange.cancel_order() is not implemented yet.")
