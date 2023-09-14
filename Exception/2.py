class Exc:
    print("program started")
    try:
        print(10 / 0)
    except TypeError:
        print("Entered into the except block handled TypeError")
    except ZeroDivisionError:
        print("Entered into the except block handled ZeroDivisionError")


print("program completed")

''' One try block can have 2 except blocks and one of the try block will execute based on the output it 
will show the result'''
