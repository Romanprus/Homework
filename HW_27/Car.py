class Car:
    def __init__(self, brand, model, year, engine, transmission):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine
        self.transmission = transmission

    def __str__(self):
        return f"Car: \n  make: {self.brand}\n  model: {self.model}  year: {self.year} with {self.engine} engine" \
               f" and {self.transmission} transmission"


if __name__ == '__main__':
    my_car = Car("Mazda", "CX-5", 2022, "Disel", "6-speed Skyactiv-MT manual")
    print(my_car)