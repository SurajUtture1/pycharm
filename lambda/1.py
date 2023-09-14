add = lambda x, y: x + y
result = add(3, 5)
print(result)

# sorting list of tuples by using lambda
points = [(1, 2), (3, 1), (0, 4)]
points.sort(key=lambda point: point[1])
print(points)

# using lambda with built in functions
numbers = [1, 2, 3, 4, 5]
# using map to double each element
douuble = list(map(lambda x: x * 2, numbers))
print(douuble)
# using filter to get even numbers
even = list(filter(lambda y: y % 2 == 0, numbers))
print(even)

v = lambda a: a + 10
print(v(5))

w = lambda a, b: a * b
print(w(5, 7))

u = lambda a, b, c: a + b + c
print(u(3, 4, 7))


# EX***********************************************************
def myfunc(n):
    return lambda a: a * n


my_doubler = myfunc(3)
print(my_doubler(11))


# ************************************************************************************************
def add(x, y):
    return x + y


lambda_add = lambda x, y: x + y
print(lambda_add(3, 4))
