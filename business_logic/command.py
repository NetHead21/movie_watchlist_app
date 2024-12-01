from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError("Command must implement an execute method")
