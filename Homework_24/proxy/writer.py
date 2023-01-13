from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def append_to_file(self, new_data):
        pass

    @abstractmethod
    def rewrite_file(self, new_data):
        pass