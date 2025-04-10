from abc import ABC, abstractmethod


class Command(ABC):
    """
    Abstract base class for commands.
    Defines the interface for all command classes.
    """

    @abstractmethod
    def run(self, exchange):
        """
        Execute the command.
        This method should be implemented by all subclasses.
        """
        pass
