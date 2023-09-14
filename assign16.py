def diff(number):
    if number > 17:
        return (number - 17) * 2
    return 17 - number


num = int(input("enter the number: "))
print("difference is %d " % diff(num))