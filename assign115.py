from functools import reduce

nums = [10, 500, 30, ]
print("original list:")
print(nums)
nums_product = reduce((lambda x, y: x * y), nums)
print("\nProduct of the said numbers (without using for loop): ",nums_product)