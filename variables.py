'''class movie:
    MovieIndustry = 'Kannada'  # STATIC VARIABLES

    def __init__(self, name, hero):
        self.name = name  # INSTANCE VARIABLES
        self.hero = hero

    def m1(self):
        x = 20  # LOCAL VARIABLES'''


''''# Static variable declare
class Test:
    a = 10

    def __init__(self):
        # self.b = 20
        Test.b = 20

    def m1(self):
        Test.c = 30

    @classmethod
    def m2(cls):
        Test.d = 90
        cls.f = 40

    @staticmethod
    def m3():
        Test.H = 60


t = Test()
t.m1()
t.m2()
t.m3()
print(Test.__dict__)'''

'''# Access static variable
class Test:
    a = 10

    def __init__(self):
        print(self.a)
        print(Test.a)

    def m1(self):
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)

    @staticmethod
    def m3():
        print(Test.a)


t = Test()
t.m1()
Test.m2()
Test .m3()
print(t.__dict__)'''


# Modifie static variable
class Test:
    a = 10

    '''@classmethod
    def m1(cls):
        cls.a = 20

    @staticmethod
    def m2():
        Test.a = 30'''

    def m3(self):
        self.a = 888


t = Test()
t.m3()
print(Test.a)  # 10 op
print(t.a)  # 888 op'''


# Test.m1()
# Test.m2()
# print(Test.a)


