import time


def timing_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        result = original_function(*args, **kwargs)
        end_time = time.time()
        print(f"{original_function.__name__} took {end_time - start_time} seconds to execute.")
        return result

    return wrapper_function()


@timing_decorator
def slow_function():
    time.sleep(2)
    print("Executed")


print(slow_function)
