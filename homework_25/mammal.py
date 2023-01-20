from abc import abstractmethod

from homework_25.Animals import Animals


class Mammals(Animals):
    def __init__(self, species: str, genus: str, diet: str, habitat: str):
        self.__genus = genus
        self.__species = species
        self.__diet = diet
        self.__habitat = habitat


    @abstractmethod
    def movement(self):
        pass

    def get_info(self):
        print(f"{self.__species} is from genus {self.__genus}, this animal eats {self.__diet}, "
              f"leaves on {self.__habitat}!")