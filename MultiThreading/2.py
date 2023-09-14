import time
import multiprocessing

'''def cal_square(numbers):
    for n in numbers:
        time.sleep(3)
        print("square:", n * n)


def cube(numbers):
    for n in numbers:
        time.sleep(5)
        print("cubes:", n * n * n)


if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=cal_square, args=(arr,))
    p2 = multiprocessing.Process(target=cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")'''

print("@#@#@#@#@#@#@#@#@#@#@#@#@#23232322#@#@#@#@#@@##@#@#@#@#@@#@#@#@#@@#@#@@#@#")

#square_result = []

'''def cal_square(numbers):
    for n in numbers:
        time.sleep(5)
        print("square:", n * n)
        square_result.append(n * n)
    print("within process: result", square_result)


if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=cal_square, args=(arr,))
    p1.start()
    p1.join()
    print("outside the process:", square_result)'''

# square: 4
# square: 9
# square: 64
# square: 81
# within process: result [4, 9, 64, 81]
''' outside the process: [] no output because: itis possible by shared memory and that memory gives you outside the 
    program result there are 2 ways to use shared memory 1 is value and 2 is array'''


# By using array
'''def cal_square(numbers, result):
    for idx, n in enumerate(numbers):
        result[idx] = n * n


if __name__ == "__main__":
    numbers = [2, 4, 7, 30]
    result = multiprocessing.Array('i', 4)
    p = multiprocessing.Process(target=cal_square, args=(numbers, result))
    p.start()
    p.join()

    print(result[:])'''


# By using value
def cal_square(numbers, result, v):
    v.value = 5.67
    for idx, n in enumerate(numbers):
        result[idx] = n * n


if __name__ == "__main__":
    numbers = [2, 4, 7, 30]
    result = multiprocessing.Array('i', 4)
    v = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=cal_square, args=(numbers, result, v))
    p.start()
    p.join()

    print(v.value)
