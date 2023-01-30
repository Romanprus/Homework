from abc import abstractmethod

from homework_25.Animals import Animals


# Inheritance and Abstraction
class Mammals(Animals):
    # encapsulation, hiding
    def __init__(self, species: str, genus: str, diet: str, habitat: str):
        self.__genus = genus
        self.__species = species
        self.__diet = diet
        self.__habitat = habitat

    # polymorphism
    # abstraction
    @abstractmethod
    def movement(self):
        pass

    def get_info(self):
        print(f"{self.__species} is from genus {self.__genus}, this animal eats {self.__diet}, "
              f"leaves on {self.__habitat}!")