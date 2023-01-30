class Train:
    def __init__(self, locomotive):
        self.locomotive = locomotive
        self.wagons = []

    def add_wagon(self, wagon):
        self.wagons.append(wagon)

    def __len__(self):
        return len(self.wagons)

    def __str__(self):
        train = "<=" + f"[HEAD <{self.locomotive}>]-"
        for wagon in self.wagons:
            train += f"{wagon}-"
        return train[:-1]


class TrainCar:
    def __init__(self, number):
        self.number = number
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < 5:
            self.passengers.append(passenger)
        else:
            print(f"Sorry mr/ms {passenger}, there are no available sits in the train wagon [{self.number}].")

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        return f"[{self.number}]"


if __name__ == '__main__':
    my_train = Train('Teplovoz')
    wagon_1 = TrainCar(1)
    wagon_2 = TrainCar(2)
    wagon_3 = TrainCar(3)
    wagon_4 = TrainCar(4)
    wagon_5 = TrainCar(5)
    wagon_6 = TrainCar(6)
    wagon_7 = TrainCar(7)
    my_train.add_wagon(wagon_1)
    my_train.add_wagon(wagon_2)
    my_train.add_wagon(wagon_3)
    my_train.add_wagon(wagon_4)
    my_train.add_wagon(wagon_5)
    my_train.add_wagon(wagon_6)
    my_train.add_wagon(wagon_7)

    wagon_1.add_passenger("Liza")
    wagon_1.add_passenger("Suzi")
    wagon_2.add_passenger("Valerchik")
    wagon_2.add_passenger("Roman")
    wagon_3.add_passenger("Dima")
    wagon_3.add_passenger("Tank Leopard")
    wagon_3.add_passenger("Donattelo")
    wagon_3.add_passenger("Rafael")
    wagon_3.add_passenger("Han Solo")
    wagon_3.add_passenger("Peter Pertigry")
    wagon_3.add_passenger("Babka")
    wagon_4.add_passenger("Boris")
    wagon_5.add_passenger("Jonson")
    wagon_7.add_passenger("Some passenger")

    print(wagon_1)
    print(wagon_6)
    print(my_train)
    print(len(wagon_1))
    print(len(wagon_2))
    print(len(wagon_3))
    print(len(wagon_7))
    print(len(wagon_5))
    print(len(my_train))
    print(wagon_4.passengers)