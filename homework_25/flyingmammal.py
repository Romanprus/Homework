from homework_25.mammal import Mammals


class FlyingMammals(Mammals):
    def __init__(self, species: str, genus: str, diet: str):
        super().__init__(species, genus, diet, 'Caves')

    def movement(self):
        print("I can fly")