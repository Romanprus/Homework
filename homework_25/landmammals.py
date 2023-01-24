from homework_25.mammal import Mammals


# Inheritance
class LandMammals(Mammals):
    def __init__(self, species: str, genus: str, diet: str):
        super().__init__(species, genus, diet, 'land')

    def movement(self):
        print("I can run")