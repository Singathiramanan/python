# LEGB Rule
# global variable
a = 10
b = 20

def func():
    return a + 1        # a is referring to global variable

def func():
    b = 20      # b is local variable
    return a + b    # a is referring to global variable

def func():
    a = 20      # a is local
    b = 20      # b is local
    return a + b

def func():
    result = a + b
    a = 20      # a is local
    b = 20      # b is local
    result = a + b
    return result


def func():
    a = a + 1
    b = b + 1
    return a + b

def func():
    # a = 20      # local variable for "func" and is enclosign scope for wrapper
    def wrapper():
        # a = 30      # local variable for wrapper
        return a + 1
    return wrapper()

def func():
    a = 10
    def wrapper():
        a = a + 1
        a = 300
    return wrapper()