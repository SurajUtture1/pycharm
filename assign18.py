def add_values(v, y, z):
    if v == y == z:
        return (v + y + z) * 3
    return v + y + z


a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))
print("Sum is : %d" % add_values(a, b, c))
