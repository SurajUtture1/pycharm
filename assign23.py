def string(str, n):
    if len(str) >= 2:
        print(str[0:1])
    elif len(str) < 2:
        count = ""
        for i in range(0, n):
            count = count + str
        return count

    else:
        print('try again.')


print(string('s', 4))
