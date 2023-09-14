def find_max_min(numbers):
    if not numbers:
        return None, None  # Return None for both max and min if the sequence is empty

    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num


# Example usage
sequence = [5, 9, 3, 1, 7, 2, 8]
max_value, min_value = find_max_min(sequence)

if max_value is not None and min_value is not None:
    print(f"Maximum value: {max_value}")
    print(f"Minimum value: {min_value}")
else:
    print("The sequence is empty.")
