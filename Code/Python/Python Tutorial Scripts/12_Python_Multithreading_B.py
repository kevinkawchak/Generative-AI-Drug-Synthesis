import threading

def function1():
    for x in range(10000):
        print("ONE")

def function2():
    for x in range(10000):
        print("TWO")

t1 = threading.Thread(target=function1)

t2 = threading.Thread(target=function2)

t1.start()
t2.start()