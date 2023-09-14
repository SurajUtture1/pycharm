import sys

str1 = "one"
str2 = "four"
str3 = "three"

x = 0
y = 112
z = 122.56
print("size of ", str1, "=", str(sys.getsizeof(str1)) + " bytes")
print("size of ", str2, "=", str(sys.getsizeof(str2)) + " bytes")
print("size of ", str3, "=", str(sys.getsizeof(str3)) + " bytes")
print("size of ", x, "=", str(sys.getsizeof(x)) + " bytes")
print("size of ", y, "=", str(sys.getsizeof(y)) + " bytes")
L = [1, 2, 3, 'Red', 'Black']
print("Size of", L, "=", sys.getsizeof(L), " bytes")
T = ("Red", [8, 4, 6], (1, 2, 3))
print("Size of", T, "=", sys.getsizeof(T), " bytes")
S = {'apple', 'orange', 'apple', 'pear'}
print("Size of", S, "=", sys.getsizeof(S), " bytes")
D = {'Name': 'David', 'Age': 6, 'Class': 'First'}
print("Size of", D, "=", sys.getsizeof(D), " bytes")
