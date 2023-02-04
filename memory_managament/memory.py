import ctypes
from gc import get_objects, collect

# # using reference counting
# a = "hello world!!"
# b = a
# c = a
# d = a

# # storing memory address of int object 360
# mem_add = id(a)

# print(ref_count(id(mem_add)))

# a = "hello"
# print(ref_count(id(mem_add)))

# b = "hi"
# print(ref_count(id(mem_add)))

# c = 1.2
# print(ref_count(id(mem_add)))

# d  = 1.8
# print(ref_count(id(mem_add)))

def ref_count(memory_address):
    """Returns the reference count of the memory address that is being passed"""
    return ctypes.c_long.from_address(memory_address).value

def is_object_in_gc(memory_address):
    for object in get_objects():
        if id(object) == memory_address:
            return True
    return False

class Manager:
    def __init__(self, name, reportee=None):
        self.name = name
        self.reportee = reportee

class Employee:
    def __init__(self, name, reporting_manager=None):
        self.name = name
        self.reporting_manager = reporting_manager

e = Employee("Steve")
m = Manager("Bob")

# noteing down the memory address of employee object and manager object
e_id = id(e)
m_id = id(m)

print(f"Reference count of employee object before cyclic reference: {ref_count(e_id)}")
print(f"Reference count of Manager object before cyclic reference: {ref_count(m_id)}")

print("--"*20)

# cyclic reference
# ----------------------------------
# # assign a reporting manager to employee
e.reporting_manager = m

# # assign a reportee to the manager
m.reportee = e
# # ----------------------------------
print(f"Reference count of employee object after cyclic reference: {ref_count(e_id)}")
print(f"Reference count of Manager object after cyclic reference: {ref_count(m_id)}")
print("--"*20)
# # make e to refer to someother object
e = "hello"

# # make m to refer to someother object
m = 1.3

print(f"Reference count of employee object after poiting to someother object: {ref_count(e_id)}")
print(f"Reference count of Manager object after pointing to someother object: {ref_count(m_id)}")
print("--"*20)

# Check if the manager and employee objects are present in Garbage Collector or not
print(is_object_in_gc(e_id))
print(is_object_in_gc(m_id))

# it clears GC
collect()

print(f"After collecing the Garbage Employee Object:{is_object_in_gc(e_id)}")
print(f"After collection the Garbage Manager Object:{is_object_in_gc(m_id)}")














