# Delete Static variable


class Test:
    r = 10

    def __init__(self):
        Test.z = 20
        del Test.r

    def m1(self):
        Test.c = 30
        del Test.z

    @classmethod
    def m2(cls):
        cls.d = 40
        del Test.c

    @staticmethod
    def m3():
        Test.e = 50
        del Test.d


t = Test()
t.m1()

Test.m2()
Test.m3()

print(Test.__dict__)
