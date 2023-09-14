'''class MyClass:
    __a = 10

    def disp(self):
        print(self.__a)


obj = MyClass()
obj.disp()


# print(obj.__a)  # private variable can't access outside the class

class MyClass:
    def __disp1(self):
        print("it is disp1")

    def disp2(self):
        print("it is disp2")
        self.__disp1()


obj = MyClass()
# obj.__disp1()  # private method not access directly outside the class if we add private method in the public method and the though public method
# we can access private method outside the class
obj.disp2()'''


class MyClass:
    __empid = 101

    def getempid(self, eid):
        self.__empid = eid
        print("it is disp1")

    def dispempid(self):
        print(self.__empid)


obj = MyClass()
obj.getempid(
    105)  # private method not access directly outside the class if we add private method in the public method and the though public method
# we can access private method outside the class
obj.dispempid()
