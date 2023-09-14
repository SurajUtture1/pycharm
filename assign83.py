num = [2, 0, 3, 4, 5]
print()
print(all(x > 1 for x in num))
print(all(x > 4 for x in num))
print(all(x > 3 for x in num))
print(all(x > 5 for x in num))
print(all(x >= 0 for x in num))
print()
