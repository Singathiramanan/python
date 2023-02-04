a = 10

def spam(some_number):
    some_number = some_number + 1
    print(some_number)

a = [10]

def spam(some_list):
    some_list.append(11)
    print(some_list)

a = "hello world"

def spam(some_string):
    some_string = some_string + "!"
    print(some_string)


d = {'a': 1, 'b': 2}

def spam(some_dict):
    some_dict['a'] = 10
    print(some_dict)


a = 10

def add(some_number=a):
    print(some_number + 1)

a = 20


def add(a, b):
    return a + b
# lambda expressions
# ananonymous functions
# inline functions
add = lambda a, b: a + b

def func(a, b):
    return a ** 2 + b ** 2 + 2 * a * b

func = lambda a , b: a ** 2 + b ** 2 + 2 * a * b

def func(a, b, c):
    return 2 * a + 3 * b + 4 * c

func = lambda a, b, c: 2 * a + 3 * b + 4 * c

def get_last_letter(string):
    return string[-1]

get_last_letter = lambda string: string[-1]

def add(a: int, b: int) -> int:
    return a + b

def greeting(name: str, age: int, pay: float) -> str:
    return f"hello {name} you are {age} years of age and you get {pay}"