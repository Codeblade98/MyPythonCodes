from time import time

def performance(func):
    def wrap(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(t2 - t1)
    return wrap


@performance
def fun1():
    for i in range(100000000):
        pass


@performance
def fun2():
    for i in list(range(100000000)):
        pass

fun1()
fun2()

