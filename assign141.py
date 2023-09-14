'''def decimal_to_hex(decimal_number):
    try:
        hex_value = hex(decimal_number)[2:]  # [2:] to remove the '0x' prefix from the hex representation
        return hex_value.upper()  # Convert to uppercase for consistency (optional)
    except TypeError:
        return "Invalid input. Please enter a valid decimal number."


if __name__ == "__main__":
    # Sample decimal numbers
    decimal_numbers = [30, 4]

    for decimal in decimal_numbers:
        hexadecimal = decimal_to_hex(decimal)
        print(f"Decimal {decimal} is equivalent to Hexadecimal {hexadecimal}")'''

h = 30
print(format(h, '02b'))
h = 4
print(format(h, '02b'))






