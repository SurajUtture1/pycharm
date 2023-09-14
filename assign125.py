import collections

num = [2, 2, 4, 4, 3, 5, 6, 7, 9, 8, 897]
print(sum(collections.Counter(num).values()))


