from json import loads

class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    # self is instance data (Internally it will be pointing to a dictionary)
    def email(self):
        return f"{self.fname}.{self.lname}@company.com"

e1 = Employee("steve", "jobs", 1000)
e2 = Employee("bill", "gates", 2000)

print(e1.email())           #   Employee.email(e1)
print(e2.email())           #   Employee.email(e2)


class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    # Alternate constructor
    @classmethod
    def from_string(cls, emp_details):      # cls is a stand-in for class reference
        words = emp_details.split(",")
        fname, lname, pay =  words
        return cls(fname, lname, pay)       # Employee("steve", "jobs", 1000)
    
    @classmethod
    def from_json(cls, response):
        # deserlisation (converting json string into python datastrcuture)
        json_obj = loads(response)
        fname = json_obj['firstname']
        lname = json_obj['lastname']
        pay = json_obj['pay']
        return cls(fname, lname, pay)

    # self is instance data (Internally it will be pointing to a dictionary)
    def email(self):
        return f"{self.fname}.{self.lname}@company.com"

# creating instance normally
e1 = Employee('bill', 'gates', 1000)

# creating object instance using string
info = "steve,jobs,2000"
e2 = Employee.from_string(info)      # Employee.from_string(Employee, info)

# creating object instance using JSON string
json_string ='{"firstname": "john", "lastname": "doe", "pay": 1000}'
e3 = Employee.from_json(json_string)

class PointAnalysis:
    def __init__(self):
        self.records = [ ]
    
    @classmethod
    def from_text_file(cls, filename):
        p = cls()       # p = Points()
        with open(filename, encoding="utf-8") as f:
            for line in f:
                parts = line.split()
                actual_record = (float(parts[0]), float(parts[1]), float(parts[2]))
                p.records.append(actual_record)
        return p
    
    @property
    def minimum(self):
        """Returns a tuple of minimum of 'x', 'y' and 'z' coordinates"""
        x_min = min([ item[0] for item in self.records ])
        y_min = min([ item[1] for item in self.records ])
        z_min = min([ item[2] for item in self.records ])
        return (x_min, y_min, z_min)
    
    @property
    def maximum(self):
        """Returns a tuple of maximum of 'x', 'y' and 'z' coordinates"""
        x_max = max([ item[0] for item in self.records ])
        y_max = max([ item[1] for item in self.records ])
        z_max = max([ item[2] for item in self.records ])
        return (x_max, y_max, z_max)
    
    @property
    def average(self):
        """Returns a tuple of average of 'x', 'y' and 'z' coordinates"""
        x_sum = sum([ item[0] for item in self.records ])
        y_sum = sum([ item[1] for item in self.records ])
        z_sum = sum([ item[2] for item in self.records ])
        return (x_sum/len(self.records), y_sum/len(self.records), z_sum/len(self.records))

import requests
import json
import csv

url = "https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true"
response = requests.request("GET", url)
data = json.loads(response.text)