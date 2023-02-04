from re import findall

class Employee:
    def __init__(self, fname, lname, pay, age):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.age = age
    
    def __setattr__(self, name, value):
        # if the user is trying to set "fname"
        if name == "fname":
            if not isinstance(value, str):
                raise Exception('fname should be of type string')
            elif len(value) < 4:
                raise Exception('Min length of fname should be 4 chars')
            elif len(value) > 5:
                raise Exception('Max length of fname should be 5 chars')
            else:
                # if everything is fine, pass the value to __setattr__ method of 
                # object class (parent class of Employee)
                super().__setattr__(name, value)
        elif name == "lname":
            if not isinstance(value, str):
                raise Exception('lname should be of type string')
            elif len(value) < 5:
                raise Exception('Min length of lname should be 5 chars')
            elif len(value) > 8:
                raise Exception('Max length of lname should be 8 chars')
            else:
                # if everything is fine, pass the value to __setattr__ method of 
                # object class (parent class of Employee)
                super().__setattr__(name, value)
        elif name == "pay":
            if not isinstance(value, (int, float)):
                raise Exception("Pay should be a Number")
            elif value < 1000:
                raise Exception("Min pay should be $1000")
            elif value > 50000:
                raise Exception('Max pay should be $50000')
            else:
                super().__setattr__(name, value)
        elif name == "age":
            if not isinstance(value, (int, float)):
                raise Exception("Age should be a number")
            elif value < 18:
                raise Exception("Min age should be 18yrs")
            elif value > 60:
                raise Exception('Max age should be 60yrs')
            else:
                super().__setattr__(name, value)


class Employee:
    def __init__(self, fname, lname, pay, age):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.age = age

    @property
    def fname(self):
        return self._fname
    
    @fname.setter
    def fname(self, value):
        print("setting")
        if not isinstance(value, str):
            raise Exception('fname should be of type string')
        elif len(value) < 4:
            raise Exception('Min length of fname should be 4 chars')
        elif len(value) > 5:
            raise Exception('Max length of fname should be 5 chars')
        else:
            self._fname = value
    
    @property
    def lname(self):
        return self._lname
    
    @lname.setter
    def lname(self, value):
        print("setting")
        if not isinstance(value, str):
            raise Exception('lname should be of type string')
        elif len(value) < 5:
            raise Exception('Min length of lname should be 5 chars')
        elif len(value) > 8:
            raise Exception('Max length of lname should be 8 chars')
        else:
            self._lname = value
        
    @property
    def pay(self):
        return self._pay
    
    @pay.setter
    def pay(self, value):
        print("setting")
        if not isinstance(value, (int, float)):
            raise Exception("Pay should be a Number")
        elif value < 1000:
            raise Exception("Min pay should be $1000")
        elif value > 50000:
            raise Exception('Max pay should be $50000')
        else:
            self._pay = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        print("setting")
        if not isinstance(value, (int, float)):
            raise Exception("Age should be a number")
        elif value < 18:
            raise Exception("Min age should be 18yrs")
        elif value > 60:
            raise Exception('Max age should be 60yrs')
        else:
            self._age = value

from validate import String, Number
# using descriptors
class Employee:
    fname = String("_fname", min_len=5, max_len=8)
    lname = String("_lname", min_len=4, max_len=6)
    age = Number("_age", min_value=18, max_value=60)
    pay = Number("_pay", min_value=2000, max_value=50000)

    def __init__(self, fname, lname, pay, age):
        self.fname = fname      # assiging some value to descriptor object ("fname")
        self.lname = lname
        self.pay = pay
        self.age = age
    
    def birthday(self):
        self.age = self.age + 1
