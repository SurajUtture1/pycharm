class Exc:
    print("program started")
    try:
        print(10 / 0)
    except TypeError:
        print("Entered into the except block handled TypeError")
    except SyntaxError:
        print("Entered into the except block handled ZeroDivisionError")
    else:
        print("Entered into else block")
    finally:
        print("Enter into finally block")


