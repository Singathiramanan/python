# Function defnition
def add(a, b, c):
    return a + b + c

# add(1, 2, 3)    # passing positional arguments
# add(2, 3, 1)
# add(a=1, b=2, c=3)  # passing keyword arguments
# add(b=2, c=3, a=1)
# add(1, b=10, c=20)
# add(1, 2, c=1.5)
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


def greeting(name, *,age, pay):
    # age and pay are keyword only arguments (MANDATORY)
    # But "name" can be either positional or keyword argument
    return f"hello {name} you are {age} years of age and you get ${pay}"

def add(*, a, b, c):
    return a + b + c

def greet(name, /, *, reverse=False, debug=False):
    if debug:
        print("You called greet function")
    if reverse:     # if reverse == True
        return f"hello {name[::-1]}"
    return f"hello {name}"


# # from zero to N
# add()
# add(1)
# add(1, 2)
# add(1, 2, 3)
# add(1, 2, 3, 4, 5)

def demo(*args):
    print(args)

def add(*args):      # function takes variable number of positional args
    total = 0
    for item in args:
        total = total + item
    return total