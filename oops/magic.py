names = ["apple", "google", "gmail"]
# Protocols
# container protocol's
# 1. __contains__()
# 2. __len__()      should return an integer
# 3. __getitem__()
# 4. __setitem__()
# 5. __delitem__()

class Point:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    
    def __len__(self):
        return 2
    
    def __contains__(self, item):
        if item == self.a or item == self.b:
            return True
        return False
    
    def __getitem__(self, index):
        """ function that returns the value at index specified """
        if index == 0:
            return self.a
        elif index == 1:
            return self.b
        else:
            raise Exception("Invalid Index")
    
    def __setitem__(self, index, value):
        if index == 0:
            self.a = value
        elif index == 1:
            self.b = value
        else:
            raise Exception("Index out of range")

class PositivePoint(Point):
    def __init__(self, a, b):
        super().__init__(a, b)

    # redefined __setitem__ in child class
    def __setitem__(self, index, value):
        if not isinstance(value, (int, float)):
            raise Exception("Only Numbers are allowed")
        if value < 0:
            raise Exception("Negative Values are not allowed")
        super().__setitem__(index, value)

class RangePoint(Point):
    def __setitem__(self, index, value):
        if index == 0:
            if value in range(0, 101):
                super().__setitem__(index, value)
            else:
                raise Exception("Only allowed range for 'a' is 0-100")
        elif index == 1:
            if value in range(0, 51):
                super().__setitem__(index, value)
            else:
                raise Exception("Only allowed range for 'b' in 0-50")
        else:
            raise Exception("Index out of range")

class Point:
    def __init__(self, *values):
        self.points = [*values]
        # self.points = list(values)
    
    def __len__(self):
        # return self.points.__len__()
        return len(self.points)
    
    def __contains__(self, item):
        return True if item in self.points else False
        # if item in self.points:
        #     return True
        # else:
        #     return False
    
    def __getitem__(self, index):
        """ function that returns the value at index specified """
        return self.points[index]
        # return self.points.__getitem__(index)       # calling __getitem__ of tuple class
    
    def __setitem__(self, index, value):
        self.points[index] = value

# Comparsion Protocols
# 1. __gt__
# 2. __eq__
# 3. __lt__

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        return False
    
    def __lt__(self, other):
        return True if self.a < other.a else False
        # s1 = self.a + self.b
        # s2 = other.a + other.b
        # return True if s1 < s2 else False
    
    def __gt__(self, other):
        return True if self.a > other.a else False
    
p1 = Point(1, 10)
p2 = Point(1, 100)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return True if self.age == other.age else False
    
    def __lt__(self, other):
        return True if self.age < other.age else False
    
    def __gt__(self, other):
        return True if self.age > other.age else False

person1 = Person("steve", 40)
person2 = Person("bill", 20)
person3 = Person("mark", 30)

# Number Protocol
# __add__
# __sub__
# __mul__
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        n1 = self.a + other.a   # 1.__add__(3)
        n2 = self.b + other.b
        return Point(n1, n2)
    
    def __sub__(self, other):
        n1 = self.a - other.a
        n2 = self.b - other.b
        # we are returning the instance of "Point" object itself with different value
        return Point(n1, n2)
    
    def __mul__(self, other):
        n1 = self.a * other.a
        n2 = self.b * other.b
        return Point(n1, n2)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = Point(5, 6)

# Attribute Protocols
# __getattribute__()
# __setattr__()
# __delattr__()

class Point:
    def __init__(self, a, b):
        self.a = a      # p.a = 1
        self.b = b      # p.b = 2

    def __setattr__(self, name, value):
        if value < 0:
            raise Exception("Negative values not allowed")
        if not isinstance(value, (int, float)):
            raise Exception("Only Numbers are allowed")
        # calling object class __setattr__ method
        super().__setattr__(name, value)

p = Point(1, 2)

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def __setattr__(self, name, value):
        super().__setattr__(name, value.upper())

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __setattr__(self, name, value):
        print(f"__setattr__ setting value for {name}")
        if not isinstance(value, (int, float)):
            raise Exception("Only numbers are allowed")
        super().__setattr__(name, value)
    
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    def __setattr__(self, name, value):
        if name == "fname" or name == "lname":
            if len(value) > 5:
                raise Exception(f"{name} should be less than 5 characters")
            super().__setattr__(name, value)
        elif name == "pay":
            if not isinstance(value, (int, float)):
                raise Exception("Only numbers are allowed for pay")
            super().__setattr__(name, value)
    
    def pay_hike(self, percentage_hike):
        hike_amount = self.pay * percentage_hike
        self.pay = self.pay + hike_amount

class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    def __setattr__(self, name, value):
        print(f"Trying to set attribute {name} to value {value}")
        if name not in ("fname", "lname", "pay"):
            raise Exception(f"Not allowed to set attribute {name}")
        super().__setattr__(name, value)

    def pay_hike(self, percentage_hike):
        hike_amount = self.pay * percentage_hike
        self.pay = self.pay + hike_amount

# immutable class
class Point:
    def __init__(self, a, b):
        print("__init__ method running")
        # this will call __setattr__ method of object class
        super().__setattr__("a", a)
        super().__setattr__("b", b)
    
    def __setattr__(self, name, value):
        raise Exception("Point class is immutable")

# print(p.a)
# print(p['a'])
# p.b -> 2
# p['b'] -> 2
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __getitem__(self, index):
        return self.__dict__[index]
        # return self.__dict__.get(index)
    # completely overriding __delattr__ method present in parent class in our child class
    def __delattr__(self, name):
        raise Exception("No you cannot delete an attribute")

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __bool__(self):
        return False if self.age < 18 else True
    
    def __len__(self): 
        return 1 if len(self.name) > 5 else 0

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __bool__(self):
        # return False if self.a == 0 and self.b == 0 else True
        return False if self.a < 0 and self.b < 0 else True

p1 = Point(1, 2)
p2 = Point(-1, 6)
p3 = Point(2, -2)
p4 = Point(-1, -3)

if p4:      # p4.__bool__()
    print("Hi")
else:
    print("Bye")

def spam():
    return "hello world"


# Greeting object is a callable becuse we have implemented __call__ method
class Greeting:
    def __init__(self, name):
        self.name = name
    
    def __call__(self):
        print(f"hello {self.name}")


class Squares:
    def __call__(self, numbers):
        squares = [ ]
        for number in numbers:
            squares.append(number ** 2)
        return squares

class Squares:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def __call__(self):
        squares = [ ]
        for number in self.numbers:
            squares.append(number ** 2)
        return squares

def log(func):
    def wrapper(*args, **kwargs):
        print(f'You are calling {func.__name__}')
        return func(*args, **kwargs)        # execuitng the original function
    return wrapper

class Log:
    # this is equivallient to outer function
    def __init__(self, func):
        self.func = func
    
    # this is equivallient to "wrapper" function
    def __call__(self, *args, **kwargs):
        print(f"You are calling {self.func.__name__}")
        return self.func(*args, **kwargs)

def _time(func):
    """Decorator measures execution time of a function"""
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Executing time: {end-start}")
        return result
    return wrapper

class Time:
    """Class Decorator which measures the execution time of a function"""
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        from time import time
        start = time()
        result = self.func(*args, **kwargs)
        end = time()
        print(f"Execution time of function {self.func.__name__} : {end-start}")
        return result

class RecordCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@RecordCalls
def add(a, b):
    return a + b

@RecordCalls
def sub(a, b):
    return a - b


items = ['bv', 'aw', 'dt', 'cu']

def get_last_char(item):
    return item[-1]

class GetLastChar:
    def __call__(self, item):
        return item[-1]

g = GetLastChar()
s = sorted(items, key=get_last_char)
s = sorted(items, key= lambda item: item[-1])
s = sorted(items, key=g)    # g('bv'), g('aw')
s = sorted(items, key=GetLastChar())    # g('bv'), g('aw')

temperatures = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]

def get_temp(item):
    return item[-1]

class GetTemp:
    def __call__(self, item):
        return item[-1]

s = sorted(temperatures, key=get_temp)
s = sorted(temperatures, key=GetTemp())

portfolio = [
                {'name': 'IBM', 'shares': 100, 'price': 91.1},
                {'name': 'AAPL', 'shares': 50, 'price': 543.22},
                {'name': 'FB', 'shares': 200, 'price': 21.09},
                {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]

def by_name(item):
    return item['name']

def by_shares(item):
    return item['shares']

def by_price(item):
    return item['price']

class By_Name:
    def __call__(self, item):
        return item['name']

class By_Shares:
    def __call__(self, item):
        return item['shares']

class By_Price:
    def __call__(self, item):
        return item['price']

class By:
    def __init__(self, by_what):
        self.by_what = by_what
    
    def __call__(self, item):
        if self.by_what == "name":
            return item['name']
        elif self.by_what == "shares":
            return item['shares']
        elif self.by_what == "price":
            return item['price']
        else:
            raise Exception("Unknown key or field name")

# s_name = sorted(portfolio, key=by_name)
# s_shares = sorted(portfolio, key=by_shares)
# s_price = sorted(portfolio, key=by_price)
by_name = By("name")
by_shares = By("shares")
by_price = By("price")

s_name = sorted(portfolio, key=by_name)
s_shares = sorted(portfolio, key=by_shares)
s_price = sorted(portfolio, key=by_price)