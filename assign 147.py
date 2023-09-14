def check_divisibility(number, divisor):
    if divisor == 0:
        return False  # Division by zero is undefined

    if number % divisor == 0:
        return True
    else:
        return False


# Accept user input for two integer values
try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    if check_divisibility(num1, num2):
        print(f"{num1} is divisible by {num2}.")
    else:
        print(f"{num1} is not divisible by {num2}.")
except ValueError:
    print("Invalid input. Please enter valid integers.")
