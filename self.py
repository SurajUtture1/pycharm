class raj:
    def __init__(delf, name, rollno, marks):
        delf.name = name
        delf.rollno = rollno
        delf.marks = marks

    def talk(delf):
        print('Hello i am:', delf.name)
        print('my roll no:', delf.rollno)
        print('my marks are:', delf.marks)


s1 = raj('sunny', 1, 99)
s2 = raj('bunny', 2, 90)
s1.talk()


class student:
    def __init__(x):
        print('cc', x)


t = student()


# argument constructor
class Test:
    def __init__(self):
        print("no arg")

    def m1(self, y):
        print("one arg")


g = Test()
h = ()


##operator overloding

class db:

    def __init__(self, name):
        self.name = name


r = db("sunny")
r.__init__("bunny")


class demo:
    def __init__(self, name):
        self.name = name


d = demo("sachin")
d.__init__("dravid")
