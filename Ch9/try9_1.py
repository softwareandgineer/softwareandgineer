class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.gas = 0

    def get_description(self):
        description = f" year = {self.year}, model = {self.model}, make = {self.make}"
        return description

    def add_gas(self, gas):
        self.gas += gas

    def run(self):
        if self.gas < 10:
            print("cannot run")
            return
        if self.gas < 10:
            self.gas = 0
        else:
            self.gas -= 10


my_car = Car("Audi", "A4", 2021)
print(my_car.get_description())

my_car.add_gas(50)

for i in range(0, 10):
    print(f"car has gas: {my_car.gas}")
    my_car.run()

class ElectricCar(Car):
    def __init__(self, make, model, year):
            super().__init__(make, model, year)
            self.battery = 0

    def run(self):
        if self.battery == 0:
            print("cannot run")
            return

        if self.battery < 1:
            self.battery = 0
        else:
            self.battery -= 5

    def charge(self, percent):
        self.battery += percent


my_ecar = ElectricCar("audi", "E3", 2022)
print(my_ecar.get_description())

my_ecar.charge(100)

for i in range(0,100):
    print(f"my electric car has battery: {my_ecar.battery}")
    my_ecar.run()
