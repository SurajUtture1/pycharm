def create_bytearray_from_integer(sample_list):
    try:
        byte_array = bytearray(sample_list)
        return byte_array
    except ValueError as e:
        print("Error:", e)
        return None


sample_list = [65, 66, 67, 255]
out = create_bytearray_from_integer(sample_list)
print(out)

