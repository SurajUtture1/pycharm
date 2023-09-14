'''# variable overriding
class Parent:
    name = "scott"


class Child(Parent):
    # name = "Suraj"
    pass


ch = Child()
print(ch.name)'''

#  Method overriding 1
'''class Bank:
    def rateofinterest(self):
        return 0


class SBIBANK(Bank):
    def rateofinterest(self):
        return 5


obj = SBIBANK()
print(obj.rateofinterest())

ob = Bank()
ob.rateofinterest()'''

#  Method overriding 2
'''class Animal:
    def Make_sound(self):
        print("common sound")


class Cat(Animal):
    def Make_Sound(self):
        #super().Make_Sound()
        print("Meow")


class Dog(Animal):
    def Make_Sound(self):
        super().Make_sound()
        print("Bark")


c = Cat()
c.Make_Sound()
d = Dog()
d.Make_Sound()'''


# Method Overloading

class Human:
    def Sayhello(self, name=None):
        if name is not None:
            print("Hello" + name)
        else:
            print("Hello")


h = Human()
h.Sayhello("raju")
h.Sayhello()

# chat gpt overloading
'''class My_class:
    def disp(self, ag, arg1):
        if arg1 is not None:
            print("One argument :", ag)
        else:
            print("two argument :", ag, arg1)


di = My_class()
di.disp(60, 64)
di.disp(20, 30)'''

'''class Bird:
    def Fly(self, name=None):
        if name == "parrot":
            print("can fly")
        if name == "penguine":
            print("cannot fly")
        if name is None:
            print("No input")


b = Bird()
b.Fly("penguine")'''

'''class A:
    def show(self):
        print("Welcome")

    def show(self, first_name=' ', number=0):
        print("Welcome", first_name, number)'''

# def show(self, first_name):
# print("Welcome", first_name)


# obj = A()
# obj.show()
# obj.show("Suraj", 3)
# obj.show("Ravi")'''

'''class Example:
    def my_method(self, arg1):
            # This is the method implementation when only one argument is passed.
            print("Method with one argument:", arg1)

    def my_method(self, arg1, arg2):        # This is the method implementation when two arguments are passed.
            print("Method with two arguments:", arg1, arg2)


obj = Example()

# Calling the method with one argument
obj.my_method(10)

# Calling the method with two arguments
obj.my_method(20, 30)'''
