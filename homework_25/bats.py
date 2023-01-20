from homework_25.flyingmammal import FlyingMammals


class Bats(FlyingMammals):
    def __init__(self, genus: str, species: str, diet: str):
        super().__init__(genus, species, diet)

    def hang_upside_down(self):
        print("I sleep upside down")

    def drink_blood(self):
        print("This type of bats drink blood)")


if __name__ == '__main__':

    bat = Bats('Desmodus rotundus', 'Chiroptera', 'mammalian blood')
    bat.get_info()
    bat.drink_blood()
    bat.hang_upside_down()
    bat.movement()



