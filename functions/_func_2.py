# Function defnition
def add(a, b, c):
    return a + b + c

add(1, 2, 3)    # passing positional arguments
add(2, 3, 1)
add(a=1, b=2, c=3)  # passing keyword arguments
add(b=2, c=3, a=1)
add(1, b=10, c=20)
add(1, 2, c=1.5)
# You cannot pass a positional argument after passing a keyword argument
# add(c=1, 3, c=10)   # invalid syntax
# add(1, b=2, 10)     # invalid syntax

# def greet(name):
#     print("You called greet function")
#     return f"hello {name}"

def add(a, b, c, debug=False):
    if debug:
        return "You called add function"
    return a + b + c

def greet(name, reverse=False):
    if reverse:     # if reverse == True
        return f"hello {name[::-1]}"
    return f"hello {name}"

def parse_string(string, delimiter=" "):
    parts = string.split(delimiter)
    return parts

# Arguments that are comming to the right of "*" is keyword only argument (Mandatory)
def greeting(name, *,age, pay):
    # age and pay are keyword only arguments (MANDATORY)
    # But "name" can be either positional or keyword argument
    return f"hello {name} you are {age} years of age and you get ${pay}"

# all the arguments in the below function are keyword only argument
def add(*, a, b, c):
    return a + b + c

# "name" is positional only argument, "reverse" and "debug" are keyword only argument
# arguments that are comming to the left of before forward slash "/" are positional only argument (Mandatory)
def greet(name, /, *, reverse=False, debug=False):
    if debug:
        print("You called greet function")
    if reverse:     # if reverse == True
        return f"hello {name[::-1]}"
    return f"hello {name}"

# All arguments are positional only arguments 
def add(a, b, c, /):
    return a + b + c


# # from zero to N
# add()
# add(1)
# add(1, 2)
# add(1, 2, 3)
# add(1, 2, 3, 4, 5)

def demo(*args):        # "*" is used to collect excess arguments or values
    print(args)

def add(*args):      # function takes variable number of positional args
    total = 0
    for item in args:
        total = total + item
    return total

def func(a, *args):
    print(a)
    print(args)

def func(*args, a):
    print(a)
    print(args)


def demo(**kwargs):
    print(kwargs)

def greet(name, **kwargs):
    print(name)
    print(kwargs)

def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)


def add(a, b, c):
    return a + b + c

numbers = (1, 2, 3)
numbers = [1, 2, 3]

# indexing
fnumber = numbers[0]
snumber = numbers[1]
tnumber = numbers[2]

# tuple unpacking
f, s, t = numbers

total = add(numbers[0], numbers[1], numbers[2]) # add(1, 2, 3)
total = add(fnumber, snumber, tnumber)      # add(1, 2, 3)
total = add(f, s, t)        # add(1, 2, 3)
total = add(*numbers)       # add(1, 2, 3)
print(total)

def add(a, b, c):
    return a + b + c

numbers = (1, 2, 3)
d = {"a": 1, "b": 2, "c": 3}

# 1. total = add(numbrs[0], numbers[1], numbers[2])
total = add(*numbers)       # add(1, 2, 3)

# 1. add(d['a'], d['b'], d['c'])
total = add(**d)        # add(a=1, b=2, c=3)    # add(x=1, y=2, z=3)

def greet():
    return "hello world"

def greeting(name):
    return f"hello {name}"

def add(a, b):
    return a + b

def mul(a, b, c):
    return a * b * c

print(greet)

# result = greet()
# print(result)