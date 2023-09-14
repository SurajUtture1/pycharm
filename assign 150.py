def has_odd_product_pair(sequence):
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] != sequence[j] and (sequence[i] * sequence[j]) % 2 != 0:
                return True
    return False


# Example usage
try:
    input_sequence = input("Enter a sequence of space-separated integers: ")
    sequence = list(map(int, input_sequence.split()))

    if has_odd_product_pair(sequence):
        print("Yes, a distinct pair of numbers with odd product is present.")
    else:
        print("No, a distinct pair of numbers with odd product is not present.")
except ValueError:
    print("Invalid input. Please enter a valid sequence of integers.")
