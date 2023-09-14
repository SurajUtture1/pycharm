import inspect


def find_module_source(module_name):
    try:
        module = __import__(module_name)
        module_file = inspect.getfile(module)
        print(f"The source file for module '{module_name}' is located at: {module_file}")
    except ImportError:
        print(f"Module '{module_name}' not found.")


# Test cases
find_module_source("math")  # Replace with the desired module name
find_module_source("random")  # Replace with the desired module name
find_module_source("nonexistent_module")  # Replace with a nonexistent module name
