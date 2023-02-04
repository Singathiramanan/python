# ======================================================================================
# Speed comparision between "is" and "==" equality operator
def compare_strings_using_is():
    """Compares two strings if there are pointing to same memory address or to the same object"""
    a = "hello_world_this_is_a_very_long_string_hello_world_this_is_a_very_long_string" 
    b = "hello_world_this_is_a_very_long_string_hello_world_this_is_a_very_long_string"
    a is b

def compare_strings_using_equality():
    """Compares two strings character by character"""
    a = "hello_world_this_is_a_very_long_string_hello_world_this_is_a_very_long_string" 
    b = "hello_world_this_is_a_very_long_string_hello_world_this_is_a_very_long_string"
    a == b
# ======================================================================================
# Speed comparision using membership operator
_set = set(range(10000000))
_list = list(range(10000000))
_tuple = tuple(range(10000000))

def membership_using_set(search_number):
    """function to check if the some number is present in the set using 'in' operator"""
    search_number in _set

def membership_using_list(search_number):
    """function to check if the some number is present in the list using 'in' operator"""
    search_number in _list

def membership_using_tuple(search_number):
    """function to check if the some number is present in the tuple using 'in' operator"""
    search_number in _tuple
# ======================================================================================
# Building a list using comprehension
def build_list_using_comprehension():
    """function to build a list of 10 million integers using comprehension""" 
    [ i for i in range(10000000) ]

def build_list_using_append():
    """function to build a list of 10 million integers using append method"""
    numbers = [ ]
    for i in range(10000000):
        numbers.append(i)
# ======================================================================================