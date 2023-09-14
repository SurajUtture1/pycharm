def in_string(text):
    if len(text) >= 2 and text[:2] == 'Is':
        return text
    return 'Is' + text


print(in_string("IArray"))
print(in_string("y"))
