from homework_25.mammal import Mammals


class WaterMammals(Mammals):
    def __init__(self, species: str, genus: str, diet: str):
        super().__init__(species, genus, diet, 'ocean')

    def movement(self):
        print("I can dive and swim")