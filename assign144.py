def check_integer_or_string(variable):
    if isinstance(variable, int):
        print("The variable is an integer.")
    elif isinstance(variable, str):
        print("The variable is a string.")
    else:
        print("The variable is neither an integer nor a string.")


# Test cases
variable1 = 42
variable2 = "Hello, World!"
variable3 = 3.14

check_integer_or_string(variable1)  # Output: The variable is an integer.
check_integer_or_string(variable2)  # Output: The variable is a string.
check_integer_or_string(variable3)  # Output: The variable is neither an integer nor a string.
