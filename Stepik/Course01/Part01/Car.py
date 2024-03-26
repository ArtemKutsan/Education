class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
   

    @classmethod
    def d(cls):
        print("HELLO")

class ElectricCar(Vehicle):
    def __init__(self, battery_size):
        # super().__init__(make, model, year) # ???
        self.battery_size = battery_size
        
my_electric_car = ElectricCar(75)
my_electric_car.d()