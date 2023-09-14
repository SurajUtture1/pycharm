'''nums = [7, 8, 9, 5]
for i in nums:
    print(i)

# use function iter and next
nums = [7, 8, 9, 5]
it = iter(nums)
print(it.__next__())
print(it.__next__())
print(next(i))'''


'''# create own iterator

class TopTen:
    def __init__(self):
        self.num = 1

    def _iter_(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration


value = TopTen()
print(next(value))

for i in value:
    print(i)
print("***************************************************************************************")'''

# Creating an iterator from a list
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

# Looping through the elements using the iterator
while True:
    try:
        element = next(my_iterator)
        print(element)
    except StopIteration:
        # The iterator raises StopIteration when there are no more elements to retrieve
        break

my_list = [1, 2, 3, 4, 5]

# Using a for loop to iterate over the list
for element in my_list:
    print(element)



