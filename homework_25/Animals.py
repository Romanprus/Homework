from abc import ABC, abstractmethod


# Abstraction
class Animals(ABC):

    @abstractmethod
    def movement(self):
        pass

    @abstractmethod
    def get_info(self):
        pass
