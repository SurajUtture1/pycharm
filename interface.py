from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def disp(self):
        pass


class Square(Shape):
    def show(self):
        print("square")

    def disp(self):
        pass


class Circle(Square):
    def disp(self):
        print("disp shape")


z = Square()
z.show()
w = Circle()
w.disp()
z.disp()
