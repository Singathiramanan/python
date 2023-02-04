from re import findall
# --------------------------
# using descriptors
# --------------------------
class Validate:
    def __init__(self, internal_variable):
        self.internal_variable = internal_variable

    def __get__(self, obj, cls):
        return obj.__dict__[self.internal_variable]
    
    def __set__(self, obj, value):
        obj.__dict__[self.internal_variable] = value

class String(Validate):
    def __init__(self, internal_variable, *, min_len=1, max_len=999999999):
        self.min_len = min_len
        self.max_len = max_len
        super().__init__(internal_variable)

    def __set__(self, obj, value):
        # is value a string or not 
        result = findall(r"^[a-zA-Z]+$", value)
        if not result:
            raise Exception("Invalid String")
        if len(value) < self.min_len:
            raise Exception(f"Min length of String should be {self.min_len}")
        if len(value) > self.max_len:
            raise Exception(f"Max length of String should be {self.max_len}")
        super().__set__(obj, value)

class Number(Validate):
    def __init__(self, internal_variable, *, min_value=0, max_value=99999999):
        self.min_value = min_value
        self.max_value = max_value
        super().__init__(internal_variable)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise Exception("not a valid number")
        if value > self.max_value:
            raise Exception(f"max value allowed is {self.max_value}")
        if value < self.min_value:
            raise Exception(f"min value allowed is {self.min_value}")
        super().__set__(obj, value)
