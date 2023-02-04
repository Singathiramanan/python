# Solution-1
class Circle:
    def __init__(self, radius):
        self.radius = radius    # self.radius = "3"
    # overriding __setattr__ method    
    def __setattr__(self, name, value):
        if not isinstance(value, (float, int)):
            raise Exception("Only Numbers are allowed")
        super().__setattr__(name, value)
    
    def circumference(self):
        return 2 * 3.14 * self.radius

# Solution-2 (using getters and setters)
class Circle:
    def __init__(self, radius):
        self.radius = radius    # self.radius = "3"
    
    # this is getter method
    @property
    def radius(self):
        return self._radius
    
    # setter method
    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Only Numbers are allowed for radius")
        self._radius = value        # creating an instance attribute "_radius" and assigning the value    

    def circumference(self):
        return 2 * 3.14 * self.radius

# Solution-1
class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    
    # over-riding __setattr__ method of object class in our child class
    def __setattr__(self, name, value):
        if name == "fname":
            if not isinstance(value, str):
                raise TypeError('Fname should be a string')
            if len(value) > 5:
                raise ValueError('fname should be less than 5 chars')
            super().__setattr__(name, value)
        elif name == "lname":
            if not isinstance(value, str):
                raise TypeError('lname should be a string')
            if len(value) > 5:
                raise ValueError('lname should be less than 5 chars')
            super().__setattr__(name, value)
        elif name == "age":
            if not isinstance(value, (int, float)):
                raise TypeError('age should be a number')
            if value > 100:
                raise ValueError('max age should be 100')
            super().__setattr__(name, value)

# Solution-2 (using getters and setters)
class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    
    @property
    def fname(self):
        print("Getter")
        return self._fname
    
    @fname.setter
    def fname(self, value):
        print("Setter")
        if not isinstance(value, str):
            raise TypeError('Fname should be a string')
        if len(value) > 5:
            raise ValueError('fname should be less than 5 chars')
        self._fname = value
    
    @property
    def lname(self):
        print("Getter")
        return self._lname
    
    @lname.setter
    def lname(self, value):
        print("Setter")
        if not isinstance(value, str):
            raise TypeError('lname should be a string')
        if len(value) > 5:
            raise ValueError('lname should be less than 5 chars')
        self._lname = value
    
    @property
    def age(self):
        print("Getter")
        return self._age
    
    @age.setter
    def age(self, value):
        print("Setter")
        if not isinstance(value, (int, float)):
            raise TypeError('age should be a number')
        if value > 100:
            raise ValueError('max age should be 100')
        self._age = value
    
    def email(self):
        return f"{self._fname}.{self._lname}@company.com"
        # return f"{self.fname}.{self.lname}@company.com"


# overriding __setattr__
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __setattr__(self, name, value):
        if name == "a" or name == "b":
            if not isinstance(value, (int, float)):
                raise ValueError
            if value < 0:
                raise ValueError
            else:
                super().__setattr__(name, value)

# using getters and setters
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("'a' must be a number")
        if value < 0:
            raise ValueError("'a' must be a positive value")
        self._a = value
    
    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("'b' must be a number")
        if value < 0:
            raise ValueError("'b' must be a positive value")
        self._b = value
    
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b

# very cheap way of doing things
class Calculator:
    def __init__(self, a, b):
        if not isinstance(a, (int, float)):
            raise TypeError("'a' must be a number")
        if a < 0:
            raise ValueError("'a' must be a positive value")
        else:
            self.a = a
        
        if not isinstance(b, (int, float)):
            raise TypeError("'b' must be a number")
        if b < 0:
            raise ValueError("'b' must be a positive value")  
        else:
            self.b = b
    
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # internal method or this method is for internal use only
    def _is_number(self, value):
        if not isinstance(value, (int, float)):
            return False
        if value < 0:
            return False
        return True
    
    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, value):
        if self._is_number(value):      # is_number(value) == True
            self._a = value
        else:
            raise ValueError()
    
    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self, value):
        if self._is_number(value):      # is_number(value) == True
            self._b = value
        else:
            raise ValueError()