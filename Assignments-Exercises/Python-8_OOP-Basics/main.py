# Car class
class Car:
    # Constructor
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Describe method 
    def describe(self):
        return f"This car is a {self.year} {self.make} {self.model}."

# Instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

prompt = my_car.describe()

print(prompt)
