# constructor
class Employee:
    def __init__(self, name, salary, project):
        self.name = name
        self.salary = salary
        self.project = project

    # method
    # to display employee details
    def show(self):
        print(self.name, self.salary)
        print("hi")

    def work(self):
        print(self.name, self.project)


# crating object of a class
emp = Employee("suraj", 800000, 'python')

# calling public method of a class
emp.show()
emp.work()


class Car:
    def __init__(self, make, model):
        self._make = make  # Protected attribute
        self.__model = model  # Private attribute

    def start_engine(self):
        print("Engine started")

    def __update_software(self):
        print("Software updated")  # Private method

    def drive(self):
        self.__update_software()
        print(self._make, self.__model)


# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla")

# Accessing public method
my_car.start_engine()

# Accessing public and protected attributes
print(my_car._make)  # Output: Toyota

# Trying to access a private attribute (Note: This will raise an AttributeError)
# print(my_car.__model)

# Trying to call a private method (Note: This will raise an AttributeError)
# my_car.__update_software()

# Accessing private attributes and methods using name mangling (for demonstration purposes only)
print(my_car._Car__model)  # Output: Corolla
# my_car._Car__update_software()  # Output: Software updated (Note: Avoid using this in real code)

# Accessing public method that indirectly calls the private method
my_car.drive()
