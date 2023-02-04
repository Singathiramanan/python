import ctypes
import gc
# ------------------------------------
# garbage collection
# ------------------------------------
# The process of freeing memory when it is not used anymore. 
# Python performs garbage collection via reference counting and a cyclic garbage collector
# that is able to detect and break reference cycles.
# The garbage collector can be controlled using the gc module.

def ref_count(address: int) -> int:
    return ctypes.c_long.from_address(address).value

def is_object_in_gc(address: int) -> bool:
    for object in gc.get_objects():
        if id(object) == address:
            return True
    return False

# --------------------------------------------------------------------------------------------
# lists pointing to each other
a = [1, 2, 3]
b = [4, 5, 6]

# get the memory address of list "a" and "b"
a_id = id(a)
b_id = id(b)

# Get the reference count
ref_count(a_id) # prints 1
ref_count(b_id) # prints 1

# Cyclic Reference
a.append(b)
b.append(a)

# Get the reference count
ref_count(a_id) # prints 2
ref_count(b_id) # prints 2

# now "a" and "b" are pointing to different objects
a = "hello"
b = "world"

# Get the reference count
ref_count(a_id) # prints 2
ref_count(b_id) # prints 2

# Check GC
is_object_in_gc(id_a)   # prints True
is_object_in_gc(id_b)   # prints True

# Clear GC
collect()

# Check GC
is_object_in_gc(id_a)   # prints False
is_object_in_gc(id_b)   # prints False

# --------------------------------------------------------------------------------------------
# Custom objects
class Manager:
    def __init__(self, name, reportee=None):
        self.name = name
        self.reportee = reportee

class Employee:
    def __init__(self, name, manager=None):
        self.name = name
        self.manger = manager

manager = Manager("Bob")
employee = Employee("Steve")

# get the memory address of manager and employee objects
id_emp = id(employee)
id_mgr = id(manager)

# This is called as "circular reference"
# assign manager to employee
employee.manager = manager

# assign employee to the manager
manager.reportee = employee

# employee object has 2 references and manager object has 2 references
ref_count(id_emp)   # prints 2
ref_count(id_mgr)   # prints 2

# delete the references to employee and manager objects
del employee
del manager

# get the reference counts (now the reference to employee and manager objects are lost).(manager and employee)
# but internally employee and manager objects are holding the references of each other (self.manager and self.reportee).
# this is called as cyclic reference. This cannot be deleted by python memory manager.
# this will be collected by garbage collecter which runs periodically.
ref_count(id_emp)   # prints 1
ref_count(id_mgr)   # prints 1

# check if these objects are present in garbage collector
is_object_in_gc(id_emp) # returns True
is_object_in_gc(id_mgr) # returns True

# manually clear the garbage collector
# both the circular references should be deleted from the garbage collector
gc.collect()
is_object_in_gc(id_emp) # returns False
is_object_in_gc(id_mgr) # returns False
# --------------------------------------------------------------------------------------------