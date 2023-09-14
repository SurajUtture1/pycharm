from multiprocessing import Pool
import time

'''def f(n):
    return n * n


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    result = []
    for n in array:
        result.append(f(n))
    print(result)'''

'''def disp(n):
    return n * n

 
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    p = Pool()
    result = p.map(disp, array)  # it will devide the work between  multiple cores
    print(result)'''  # reduce aggregate these works in single unit


def show(n):
    sum = 0
    for x in range(1000):
        sum += x + x
    return sum


if __name__ == "__main__":
    t1 = time.time()  # starting time
    p = Pool()  # object of pool class
    result = p.map(show, range(100000))
    p.close()
    p.join()

    print("POOL TOOK:", time.time() - t1)
    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(show(x))
    print("serial processing took: ", time.time() - t2)


def sur(n):
    return n * n


if __name__ == "__main__":
    p = Pool(processes=3)
    result = p.map(sur, [1,2])
    for n in result:
        print(n)

'''def sum_numbers_in_range(start, end):
    total = 0
    for number in range(start, end + 1):
        total += number
    return total

# Call the function to sum numbers in the range of 1 to 1000
result = sum_numbers_in_range(1, 1000)
print("Sum of numbers from 1 to 1000:", result)'''
