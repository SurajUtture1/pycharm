import multiprocessing


def cal_square(numbers, q):  # child process
    for n in numbers:
        q.put(n * n)


if __name__ == "__main__":  # Parent process
    numbers = [2, 3, 5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=cal_square, args=(numbers, q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())


#python has a module called q and q module is different than multiprocessing q so 
