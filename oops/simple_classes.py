a = [1, 2]
t = (1, 2)

# add two numbers
total = a[0] + a[1]

# adding something to the first and second items
a[0] = a[0] + 0.5
a[1] = a[1] + 0.5

# swap two integers stored in the list
temp = a[0]
a[0] = a[1]
a[1] = temp

# reset the co-ordinates
a[0] = 0
a[1] = 0

# a class is a collection of functions that carryout vaiours operations or manuplates 
# data (instance)
class Point:
    # constructor or init method or magic method
    # responsible for saving the data inside a dictionary 
    # this dict is called as instance disctionary
    # you can access the instance dict via an attribute __dict__
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # "self" is data or internally it will be pointing to a dictionary
    def move(self, dx, dy):
        self.a = self.a + dx
        self.b = self.b + dy
    
    def reset(self):
        self.a = 0
        self.b = 0
    
    def sort(self):
        if self.a < self.b:
            return (self.a, self.b)
        return (self.b, self.a)
    
    def swap(self):
        temp = self.a
        self.a = self.b
        self.b = temp
        return (self.a, self.b)
    
    def total(self):
        return self.a + self.b

# data or instance
# you are creating an instance of point class
p1 = Point(1, 2)
p2 = Point(4, 3)
p3 = Point(100, 200)

# p1.reset()      # Point.reset(p1)
# p2.reset()      # Point.reset(p2)
# p3.reset()      # Point.reset(p3)

# Point.move(p1, 0.1, 0.1)

# Point.move(p2, 0.5, 0.5)

class Arithmetic:
    # saving two integers inside instance dictionary
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b 


a1 = Arithmetic(1, 2)
a2 = Arithmetic(3, 4)
a3 = Arithmetic(5, 6)


# employee1 = ['steve', 'jobs', 26, 1000]
# employee2 = ('steve', 'jobs', 26, 1000)

# employee3 = {"fname": "steve", "lname": "jobs", "age": 26, "pay": 1000}
# employee4 = {"fname": "bill", "lname": "gates", "age": 28, "pay": 2000}

class Employee:
    def __init__(self, fname, lname, age, pay):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.pay = pay

    # instance method
    def email(self):
        return f"{self.fname}.{self.lname}@company.com"

    def pay_hike(self, percentage):
        hike = self.pay * percentage
        self.pay = self.pay + hike

e1 = Employee("steve", "jobs", 26, 1000)
e2 = Employee("bill", "gates", 28, 2000)

class Point:
    # overloaded constructor
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

p1 = Point()        # Point.move(p1)    p1.move()
p2 = Point(1)       # Point.move(p2)        p2.move()
p3 = Point(1, 2)        # Point.move(p3)    p3.move()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
    
    def attack(self, pts):
        self.health -= pts

p1 = Player(1, 2)
p2 = Player(2.3, 1.4)

# "self" is first argument of any method inside the class
# it need not be named or called as "self". You can give any name to that argument
# But by convention in python, it is normally called as "self"
# "self" will be internally pointing to instance dictionary or it is also called as "instance" or "data"
