from csv import reader, DictReader
# with open("/Users/sandeep/Desktop/Training/_python/data_files/employees.csv", "r") as f:
#     rows = reader(f)        # rows is a generator
#     next(rows)  # advance by one row
#     for row in rows:    # feed the generator to for loop
#         print(row[0], row[3])

# with open("/Users/sandeep/Desktop/Training/_python/data_files/employees.csv", "r") as f:
#     rows = DictReader(f)        # rows is a generator
#     for row in rows:    # feed the generator to for loop
#         print(row['fname'], row['gender'])

# count = {'Male': 5, 'Female': 3}


def read_csv():
    """
    Reads the contents of the csv file into a list
    Each record of the list is a dictionary
    """
    records = [ ]
    with open("../data_files/employees.csv") as f:
        rows = DictReader(f)
        for row in rows:
            records.append(row)
    return records

# I want to know the total pay that i am paying to all the employees as salary
def total_pay_to_employees():
    """Returns the total amount that is paid to all the employees as salary"""
    total = 0.00
    data = read_csv()
    for item in data:
        total = total + float(item['pay'])
    return total

# i want to know how many male and females employees are working in the company
def count_by_gender():
    """This function returns a dictionary with count of male and female employees"""
    data = read_csv()
    by_gender = { }
    for item in data:
        gender = item['gender']
        if gender in by_gender:
            by_gender[gender] += 1
        else:
            by_gender[gender] = 1
    return by_gender

# highest and least paid employee
def highest_and_lowest_pay():
    """Returns a tuple of highest and least paid employee records"""
    data = read_csv()
    sorted_emps = sorted(data, key=lambda item: item['pay'])
    return (sorted_emps[0], sorted_emps[-1])

def pay_more_4500():
    """Returns list of employees who gets more than $4500 as salary"""
    emps = [ ]
    data = read_csv()
    for item in data:
        if float(item['pay']) > 4500:
            emps.append(item)
    return emps

def unique_teams():
    """Returns set of unique teams"""
    teams = set()
    data = read_csv()
    for item in data:
        teams.add(item['team'])
    return teams

def unique_teams():
    """Returns set of unique teams"""
    data = read_csv()
    # using set comprehension
    teams = {  item['team'] for item in data }    
    return teams
