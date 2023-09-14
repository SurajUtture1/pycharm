def enter_age(age):
    if age < 0:
        raise ValueError("positive integer allowed")

    if age % 2 == 0:
        print("age is even")

    else:
        print("age is odd")


try:
    num = -5
    enter_age(num)
except ValueError:
    print("positive allowed")
except:
    print("something wrong")
