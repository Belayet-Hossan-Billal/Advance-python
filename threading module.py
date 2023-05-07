"""
import threading
def print_hello(num):
    print("you are an employee", num)
t1 = threading.Thread(target=print_hello("num"), args=(10))
t1.start()
t1.join()
print("End")

"""

# Multithreading with two Threads
import threading
def print_one():
    for i in range(2):
        print(1)
def print_two():
    for i in range(2):
        print(2)
if __name__ == "__main__":

    t1 = threading.Thread(target=print_one())
    t2 = threading.Thread(target=print_two())

t1.start()
t2.start()
t1.join()
t2.join()
print("completed!")
