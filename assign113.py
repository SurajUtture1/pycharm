while True:

    try:
        a=int(input("Enter a number: "))
        break
    except ValueError:
        print("\nThis is not a number. try again...")
        print()