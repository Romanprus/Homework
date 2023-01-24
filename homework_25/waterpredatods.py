from homework_25.watermammal import WaterMammals


# Inheritance
class WaterPredator(WaterMammals):
    def __init__(self, genus: str, species: str, diet: str):
        super().__init__(genus, species, diet)

    @staticmethod
    def hunt():
        print("I can hunt fish or human")


if __name__ == '__main__':
    Shark = WaterPredator('Shark', 'Chondrichthyes', 'Fish or Humans')
    Shark.get_info()
    Shark.hunt()
    Shark.movement()