# a decorator is a callable which adds some extra functionality to the existing
# function without modifying the original function
def log(some_other_func):
    def wrapper(*args, **kwargs):
        # this is the extra functionality that the decorator is adding
        print(f"Hey there You called {some_other_func.__name__} function")
        # actual function is getting executed here
        result = some_other_func(*args, **kwargs)
        return result
    return wrapper

from time import sleep, time
def delay(func):
    def wrapper(*args, **kwargs):
        sleep(5)    # some extra func
        result = func(*args, **kwargs)  # original func
        return result
    return wrapper

def positive(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return abs(result)
    return wrapper

def exe_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"execution time {end-start}")
        return result
    return wrapper

# @exe_time
def greet():
    sleep(3)
    return "hello world"

@exe_time
def add(a, b):
    sleep(10)
    return a + b

@exe_time
def mul(a, b):
    sleep(15)
    return a * b
