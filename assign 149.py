def sum_of_cubes(n):
    if n <= 0:
        return 0  # Return 0 for non-positive integers

    total = 0
    for i in range(1, n):
        total += i ** 3
    return total


# Example usage
try:
    num = int(input("Enter a positive integer: "))
    if num > 0:
        result = sum_of_cubes(num)
        print(f"The sum of cubes of positive integers smaller than {num} is: {result}")
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
