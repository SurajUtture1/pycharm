'''class Exc:
    print("program started")
    a = 10
    b = 0
    c = a/b'''


class Exc:
    print("program started")
    a = 10
    b = 0 
    try:
        c = a / b
    except:
        print("handled")
