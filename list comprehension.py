even_squares = [x ** 2 for x in range(10) if x % 2 != 0]
print(even_squares)

fruits = ["apple", "banana", "kiwi", "cherry", "mango"]
new_list = []

for x in fruits:
    if "b" in x:
        new_list.append(x)

print(new_list)

new_list = [x for x in fruits if x != "apple"]
print(new_list)

new_list = [x for x in range(10)]
print(new_list)

new_list = [x.upper() for x in fruits]
print(new_list)

new_list = ["hello" for x in fruits]
print(new_list)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
