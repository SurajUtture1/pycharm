# Using Unicode code points
unicode_code_points = [0x2764, 0x1F601, 0x1F4A1, 0x1F680]

print("Printing Unicode characters using Unicode code points:")
for code_point in unicode_code_points:
    print(chr(code_point), end=" ")

print("\n")

# Using escape sequences
unicode_escape_sequences = ['\u2764', '\U0001F601', '\U0001F4A1', '\U0001F680']

print("Printing Unicode characters using escape sequences:")
for escape_sequence in unicode_escape_sequences:
    print(escape_sequence, end=" ")
