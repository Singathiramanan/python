# parent is inheriting from "object" class
class Parent(object):
    def __init__(self, value):
        self.value = value
    
    def apple(self):
        print('this is a new addition')
        print(f'executing parent class apple method {self.value}')
    
    def google(self):
        print('executing parent class google method')
        self.apple()

# case-1 (child inherits from parent, and child has completely independent method)    
class Child1(Parent):
    # child class is initlising the parent class constructor
    # because it's child class's responsibility to initlise the parent class constructor
    # if the child is inheriting from parent
    # super() is a function which is used to access parent class attribute's
    def __init__(self, value):
        super().__init__(value)     # we are calling parent class constructor
        # Parent.__init__(self, value)

    def yahoo(self):
        print("executing child1 yahoo")

# case:2 child class re-defining parent class method or over-riding parent class method
# Completely re-defining "apple" in Child2
class Child2(Parent):
    def __init__(self, value):
        super().__init__(value)
    
    # we are actually re-defining "apple" method in child2 class
    def apple(self):
        print('Executing child2 apple method')

# MRO - Method Resolution Order
# it is the order in which python searches or look's up for an attribute in inheritance hierarchy

# case-3: 
# re-defining "apple" method in child3, but re-using the original functionality provided by
# "apple" method in Parent class
class Child3(Parent):
    def __init__(self, value):
        super().__init__(value)
    
    def apple(self):
        print('some extra stuff in child3')
        super().apple() # giving a call to parent class "apple" method

# case-4 Child class having an extra attribute in __init__ method
class Child4(Parent):
    def __init__(self, value, extra_value):
        # Parent.__init__(self, value)
        super().__init__(value)     # this is an attribute of Parent class __init__
        self.extra_value = extra_value  # extra attribute of child4
    
    def facebook(self):
        print(f"some extraa thing {self.extra_value}")

# case-5 Child inheriting from multiple parents
class Parent2:
    def __init__(self, some_value):
        self.some_value = some_value
    
    def facebook(self):
        print(f"parent2 facebook {self.some_value}")

# case-6 Multiple Inheritance
class Child5(Parent, Parent2):
    def __init__(self, value, some_value):
        Parent.__init__(self, value)
        Parent2.__init__(self, some_value)
    
    def instagram(self):
        print("Child5 Instagram")

# Multi-level inheritance
class A:
    def demo(self):
        print('A')

class B(A):
    def demo(self):
        print('B')
        super().demo()

class C(B):
    def demo(self):
        print("C")
        super().demo()

class Spam:
    a = 10
    def apple(self):
        print(f"executing Spam apple {self.__class__.a}")        # Spam.a

class Demo(Spam):
    # we are actually overriding the class variable
    # a = 20      # Re-defining class variable "a"
    def google(self):
        # print(f"Demo google {self.__class__.a}")
        # print(f"Demo google {Spam.a}")
        print(f"Demo google {Demo.a}")