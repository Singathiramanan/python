from time import sleep, time

# a decorator is a callable which adds some extra functionality to the existing
# function without modifying the original function
def log(some_other_func):
    def wrapper(*args, **kwargs):
        # this is the extra functionality that the decorator is adding
        print(f"Hey there You called {some_other_func.__name__} function")
        # actual function is getting executed here
        result = some_other_func(*args, **kwargs)   # original add(1, 2) func
        # add(a=1, b=2)
        return result
    return wrapper

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

# solution:1
def positional_only(func):
    def wrapper(*args):
        result = func(*args)
        return result
    return wrapper

# solution:2
def positional_only(func):
    def wrapper(*args, **kwargs):
        if len(kwargs) == 0:
            result = func(*args, **kwargs)
            return result
        raise Exception("Only Positional arguments are allowed")
    return wrapper

def keyword_only(func):
    def wrapper(*args, **kwargs):
        if len(args) == 0:
            result = func(*args, **kwargs)
            return result
        raise Exception("Only keyword arguments are allowed")
    return wrapper

def greet():
    sleep(1)
    return "hello world"




word = "helloworld"
# {"h": 1, "e": 1, "l": 3, }...
# solution1:
letter_count_pair = { }
for letter in word:
    letter_count_pair[letter] = word.count(letter)

#solutoion 2:
_letter_count_pair = { }

for letter in word:
    # chekcing if the character is already present as a key of a dict or not
    # if the key is already present in the dictionary, get the current value
    # of that key and increment the count by 1
    if letter in _letter_count_pair:
        _letter_count_pair[letter] = _letter_count_pair[letter] + 1
    # if the key does not exist, goahead and create a key with that character
    # and initlise the value to 1. Becuse this is the first time we are encountering 
    # that character or key
    else:
        _letter_count_pair[letter] = 1

sentence = "hello hi there hello hi hi hi hello"
# {"hello": 3, "hi": 4}

word_count_pair = { }
words = sentence.split()

for word in words:
    if word in word_count_pair:
        word_count_pair[word] = word_count_pair[word] + 1
    else:
        word_count_pair[word] = 1

def cache(func):
    _cache = { }    # empty dictionary
    print(_cache)
    def wrapper(*args):
        if args in _cache:
            return _cache[args]
        result = func(*args)
        _cache[args] = result
        return result
    return wrapper

# dictionary to keep track of function name and its count
func_calls = { }

def count_calls(func):
    def wrapper(*args, **kwargs):
        if func.__name__ in func_calls:
            func_calls[func.__name__] = func_calls[func.__name__] + 1
        else:
            func_calls[func.__name__] = 1
        result = func(*args, **kwargs)
        return result
    return wrapper

func_calls = { }

def max_calls(func):
    def wrapper(*args, **kwargs):
        if func.__name__ in func_calls:
            func_calls[func.__name__] = func_calls[func.__name__] + 1
        else:
            func_calls[func.__name__] = 1
        if func_calls[func.__name__] <= 5:
            result = func(*args, **kwargs)
            return result
        raise ValueError('Cannot call a function more than 5times')
    return wrapper

@log("hello there you called add function")
def add(a, b):
    return a + b

@log("hi how are you doing")
def mul(a, b):
    return a * b