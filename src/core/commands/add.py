from .base import Command


class AddCommand(Command):
    def __init__(self, order):
        """
        Initialize the AddCommand with an order.
        :param order: The order to be added.
        """
        self.order = order

    def run(self, exchange):
        """
        Execute the command to add an order to the exchange.
        :param exchange: The exchange to which the order will be added.
        """
        raise NotImplementedError("Exchange.add_order() is not implemented yet.")
