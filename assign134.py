'''print("Input the value of x & y ")
x, y = map(int, input().split())
print("The value of x & y are: ", x, y)'''


def main():
    try:3
        # Input two integers on a single line, separated by a space
        input_line = input("Enter two integers separated by a space: ")

        # Split the input line into two parts
        num1, num2 = map(int, input_line.split())

        # Print the input integers
        print("First integer:", num1)
        print("Second integer:", num2)

    except ValueError:
        print("Invalid input! Please enter two integers separated by a space.")


if __name__ == "__main__":
    main()
