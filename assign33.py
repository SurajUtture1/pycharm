def sun(x, y, z):
    if x == y or y == z or z == x:
        sun = 0
    else:
        sun = x + y + z
    return sun


print(sun(2, 2, 2))
print(sun(2, 3, 2))
print(sun(3, 2, 5))
