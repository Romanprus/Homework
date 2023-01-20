from homework_25.landmammals import LandMammals


class Predator(LandMammals):
    def __init__(self, genus: str, species: str, diet: str):
        super().__init__(genus, species, diet)

    def __sit_in_ambush(self):
        print("I'm prepare to atack")


    def __catch_pray(self):
        print("i catch pray")

    def hunt(self):
        self.__sit_in_ambush()
        self.__catch_pray()
        print("I can hunt")


if __name__ == '__main__':
    gepard = Predator('Gepard', 'Felidae', 'meat')
    gepard.get_info()
    gepard.movement()
    gepard.hunt()