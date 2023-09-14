'''def repeat_decorator(repeat_times):
    def actual_decorator(original_function):
        def wrapper_function(*args, **kwargs):
            for _ in range(repeat_times):
                result = original_function(*args, **kwargs)
            return result

        return wrapper_function

    return actual_decorator


@repeat_decorator(repeat_times=3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")'''

numbers = [1, 4, 3, 6, 5]
subset = numbers[1:3]
print(subset)

numbers[2] = 6
print(numbers)

numbers.append(8)
print(numbers)

names = ["Suraj", "Raju", "Rani"]
names.insert(1, "Eye")
print(names)
names.remove("Eye")
print(names)

length = len(names)
print(length)

combined = numbers + names
print(combined)

repeated = numbers * 3
print(repeated)

num = numbers.sort()
print(num)

numbers = {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
r = set1 ^ set2
print(r)
if 2 in set1:
    print("2 is there")

squares = {x ** 2 for x in range(1, 6)}
print(squares)


# suraj.py
def greet(name):
    return f"Hello, {name}"



