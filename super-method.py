class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print("Vehicle is being driven.")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        super().drive()
        print(f"{self.brand} {self.model} is being driven.")

my_car = Car("Toyota", "Camry")
my_car.drive()
