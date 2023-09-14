def check_variable_type(variable):
    if isinstance(variable, list):
        return "List"
    elif isinstance(variable, tuple):
        return "Tuple"
    elif isinstance(variable, set):
        return "Set"
    else:
        return "Unknown"

# Test cases
var1 = [1, 2, 3]
var2 = (4, 5, 6)
var3 = {7, 8, 9}
var4 = "string"

print(f"Variable 1 is a {check_variable_type(var1)}")
print(f"Variable 2 is a {check_variable_type(var2)}")
print(f"Variable 3 is a {check_variable_type(var3)}")
print(f"Variable 4 is a {check_variable_type(var4)}")

