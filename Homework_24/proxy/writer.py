from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def append_to_file(self):
        pass

    @abstractmethod
    def rewrite_file(self):
        pass