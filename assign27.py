def concatenate_list(lists):
    result = ''
    for element in lists:
        result += str(element)
    return result


print(concatenate_list(["Suraj", "age", "is", 27]))
