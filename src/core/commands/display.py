from .base import Command


class DisplayCommand(Command):
    def run(self):
        """
        Execute the command to display a message.
        :param exchange: The exchange on which the message will be displayed.
        """
        raise NotImplementedError("Exchange.display_message() is not implemented yet.")
