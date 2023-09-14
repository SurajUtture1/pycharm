# super by method
class A:
    def m1(self):
        print("i am method from A")


class B(A):
    def m2(self):
        print("i am method from B")
        super().m1()


obj = A()
obj.m1()
obj1 = B()
obj1.m2()
print("********")

########################################################

# super by variable
a, b = 15, 20


class A:
    m, n = 10, 20


class B(A):
    a, b = 60, 80

    def m1(self, i, j):
        print(i + j)
        print(self.a + self.b)
        print(super().m + super().n)
        print(globals()['a'] + globals()['b'])


objr = B()
objr.m1(70, 70)
print("******************************************************************************")


# super by constructor
class A:
    def __init__(self):
        print("from A")


class B(A):
    def __init__(self):
        print("from B")
        super().__init__()
        A.__init__(self)


bobh = B()
