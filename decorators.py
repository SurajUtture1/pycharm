'''def outer():
    x = 3

    def inner():
        y = 3
        result = x + y
        return result

    return inner()


a = outer()
print(a)'''


# use one function parameter as another function
def function1():
    print('i am function 1')


def function2(func):
    print("i am function 2")
    func()


function2(function1)


# decorator
def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()

    return inner


@str_upper
def print_str():
    return "good morn"


print(print_str())


# fun in fun with parameter
def div_s(func):
    def inner(x, y):
        if y == 0:
            return "give proper input"
        return func(x, y)

    return inner


def div(a, b):
    return a / b


print(div(4, 1))


