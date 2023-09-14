nums = [56, 89, -40, 0, -60, 60, -80]
print("original list: ", nums)
new_nums = list(filter(lambda x: x >= 0, nums))
print("positive numbers from list: ", new_nums)
