'''from threading import Thread
from time import sleep


class A(Thread):
    def run(self):
        for i in range(5):
            print("Akhilesh")
            sleep(2)



class B(Thread):
    def run(self):
        for i in range(5):
            print("Akshata")
            sleep(1)


t1 = A()
t2 = B()
#t1.run()
#t2.run()
t1.start()
t2.start()
t1.join()
t2.join()

print("Suraj")'''

from threading import Thread


def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")


def print_letters():
    for letter in 'abcde':
        print(f"Letter: {letter}")


# Create thread objects
t1 = target = print_numbers
t2 = target = print_letters

t1.start()
t2.start()
