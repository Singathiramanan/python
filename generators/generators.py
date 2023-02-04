# Normal Function
def func():
    print("executing function")
    return 1
    return 2
    return 3

# Generator function
def func_():
    print("Generator executing")
    yield 1
    yield 2
    yield 3

def _func():
    """generator function"""
    print("hello")
    print('how are you')
    a = 2
    print(a)
    yield "hi"      # the control gets supsped or paused here
    print("world")
    yield "bye"

# normal function
def evens():
    e = [ ]
    for i in range(21):
        if i % 2 == 0:
            e.append(i)
    return e

# generator function (lazy iterables)
def g_evens():
    for i in range(21):
        if i % 2 == 0:
            yield i

def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        next_number = a + b
        a = b
        b = next_number

# def fibonacci():
#     a = 0
#     b = 1
#     f = [ ]
#     while True:
#         f.append(a)
#         next_number = a + b
#         a = b
#         b = next_number
#     return f

names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']

def vowels():
    v = [ ]
    for name in names:
        if name[0] in 'aeiou':
            v.append(name)
    return v

def vowels():
    for name in names:
        if name[0] in 'aeiou':
            yield name
    
def frange(start, stop, step):
    while start <= stop:
        yield start
        start = start + step

# list comprehension
e = [ i  for i in range(0, 21) if i % 2 == 0 ]

# normal function
def evens():
    e = [ ]
    for i in range(0, 21):
        if i % 2 == 0:
            e.append(i)
    return e

# generator function (lazy iterables)
def g_evens():
    for i in range(21):
        if i % 2 == 0:
            yield i
            
# this is called as generator expression
g = ( i  for i in range(0, 21) if i % 2 == 0 )

names = ["apple", "google", "yahoo", "gmail", "flipkart", "yelp"]
# [("apple", 5), ("google", 6), ("yahoo", 5)]

# using normal list append
def item_len_pair():
    items = [ ]
    for name in names:
        items.append((name, len(name)))
    return items

# using list comprehension
items = [ (name, len(name))  for name in names ]

# using generator function
def g_items():
    for name in names:
        yield (name, len(name))

# generator expression
g = ( (name, len(name))  for name in names )