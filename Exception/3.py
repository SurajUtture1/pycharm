class Exc:
    print("program started")
    try:
        print(10 / 2)
    except TypeError:
        print("Entered into the except block handled TypeError")
    except ZeroDivisionError:
        print("Entered into the except block handled ZeroDivisionError")
    else:
        print("Entered into else block")