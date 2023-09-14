class Example:
    def my_method(self, arg1):
        # This is the method implementation when only one argument is passed.
        print("Method with one argument:", arg1)

    def my_method(self, arg1, arg2):  # This is the method implementation when two arguments are passed.
        print("Method with two arguments:", arg1, arg2)


obj = Example()

# Calling the method with one argument
obj.my_method(10)
obj.my_method(10, 20)
