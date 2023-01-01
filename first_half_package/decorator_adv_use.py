
from time import time
def performance(fun):
    def wrap(*args, **kwargs):
        time_initial = time()
        result = fun(*args, **kwargs)
        time_final = time()
        print(f'\nThe function took {time_final - time_initial} seconds to run')
    return wrap

@performance
def long_time():
    for time in range(1, 100000000):
        pass


@performance
def short_time():
    for time in range(1,10000):
        pass

long_time()
short_time()