from abc import ABC, abstractmethod


class Car(ABC):
    def show(self):
        print("every car had 4 wheels")

    @abstractmethod
    def speed(self):
        pass


class Hundai(Car):
    def speed(self):
        print("speed 100km/hr")


class Suzuki(Car):
    def speed(self):
        print("very fast")


h = Hundai()
h.speed()
h.show()
S = Suzuki()
S.speed()
S.show()


# Data abstraction
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def drive(self):
        print(f"{self.make} {self.model} is driving.")


# Creating objects
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Using abstraction
car1.start()
car2.drive()



