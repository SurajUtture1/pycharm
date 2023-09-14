# Single level inheritance
class A:

    def m1(self):
        print("this method is from A")


class B(A):

    def m2(self):
        print("This is from B")


aobj = A()
aobj.m1()

bobj = B()
bobj.m1()
bobj.m2()
print("******")


class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)


class B(A):
    a, b = 50, 20

    def m2(self):
        print(self.a + self.b)


obj1 = A()
obj1.m1()
obj2 = B()
obj2.m1()
obj2.m2()


# Multilevel inheritance

class A:
    x, y = 100, 200

    def m1(self):
        print(self.x + self.y)


class B(A):
    a, b = 500, 200

    def m2(self):
        print(self.a + self.b)


class C(B):
    r, s = 500, 200

    def m3(self):
        print(self.r + self.s)


obj1 = A()
obj1.m1()
obj2 = B()
obj2.m1()
obj2.m2()
obj3 = C()
obj3.m1()
obj3.m2()
obj3.m3()


# Hirarchical
class A:
    x, y = 100, 200

    def m1(self):
        print(self.x + self.y)


class B(A):
    a, b = 500, 200

    def m2(self):
        print(self.a + self.b)


class C(A):
    r, s = 600, 200

    def m3(self):
        print(self.r + self.s)


obj1 = A()
obj1.m1()
obj2 = B()
obj2.m1()
obj2.m2()
obj3 = C()
obj3.m1()
obj3.m3()


# multiple
class A:
    x, y = 100, 200

    def m1(self):
        print(self.x + self.y)


class B(A):
    a, b = 500, 200

    def m2(self):
        print(self.a + self.b)


class C(B, A):
    r, s = 500, 200

    def m3(self):
        print(self.r + self.s)


obj1 = A()
obj1.m1()
obj2 = B()
obj2.m1()
obj2.m2()
obj3 = C()
obj3.m1()
obj3.m2()
obj3.m3()

import rs

print(rs.greet("suraj"))


class Employee:
    def __init__(self, emp_name, emp_sal, emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_sal = emp_sal

    def display_info(self):
        print(self.emp_sal, self.emp_id, self.emp_name)


class Manager(Employee):
    def __init__(self, emp_name, emp_sal, emp_id, department):
        super().__init__(emp_name, emp_sal, emp_id)
        self.department = department

    def display_info(self):
        super().display_info()
        print(self.department)


class Engineer(Employee):
    def __init__(self, emp_id, emp_sal, emp_name, language):
        super().__init__(emp_name, emp_sal, emp_id)
        self.language = language

    def display_info(self):
        super().display_info()
        print(self.language)


man = Manager("Suraj", 800000, 1, 'Mech')
man.display_info()
Eng = Engineer(2, 870000, "Raju", 'Python')
Eng.display_info()


class Anima:
    def __init__(self, walk, eat):
        self.walk = walk
        self.eat = eat

    def info(self):
        print(self.walk, self.eat)


class Bird(Anima):
    def __init__(self, walk, fly):
        super().__init__(walk)
        self.fly = fly

    def __int__(self):
        super().info()
        print(self.fly)


class Fish(Anima):
    def __int__(self, walk, eat, swim):
        super().__init__(self, walk)
        self.swim = swim

    def info(self):
        super().info()
        print(self.swim)


B = Bird("200m", "Ants", "High")
B.info()
F = Fish("300m", "weg", "far")
F.info()
