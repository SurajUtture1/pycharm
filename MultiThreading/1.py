import threading
import time


def cal_numbers(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("square:", n * n)


def cal_cube(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("cubes:", n * n * n)


arr = [2, 4, 8, 9]
t = time.time()

t1 = threading.Thread(target=cal_numbers, args=(arr,))
t2 = threading.Thread(target=cal_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

cal_numbers(arr)
cal_cube(arr)
print("done in: ",time.time()-t)
print("work completed")
