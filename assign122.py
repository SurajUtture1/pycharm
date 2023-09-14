def empty_variable(var):
    if isinstance(var, (int, float)):
        return 0
    elif isinstance(var, dict):
        var.clear()
        return var
    else:
        return var

# Sample data
n = 20
d = {"x": 200}

# Emptying the variables
n = empty_variable(n)
d = empty_variable(d)

# Printing the output
print(n)  # Output: 0
print(d)  # Output: {}