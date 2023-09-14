length = int(input("Enter list length : "))
my_list = []
for _ in range(length):
    temp = int(input("Enter list item : "))
    my_list.append(temp)

    four_count = my_list.count(4)

    print("Number 4 occurs", four_count, "times.")
