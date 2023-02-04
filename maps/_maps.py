numbers = [1, 2, 3, 4, 5]
squares = [ ]
for number in numbers:
    squares.append(number ** 2)

# usingh comprehension
squares = [number ** 2 for number in numbers]

def square_number(number):
    return number ** 2

m = map(square_number, numbers)

names = ['apple', 'google', 'yahoo', 'gmail', 'facebook', 'yelp', 'microsoft', 'instagram']

item_len_pair = []

for name in names:
    item_len_pair.append((name, len(name)))

# map
def get_name_len_pair(name):
    return (name, len(name))

# using lambda function
m = map(lambda name: (name, len(name)), names)

m = map(get_name_len_pair, names)

str_nums = ["1", "2", "3", "4"]

int_nums = [ int(item) for item in str_nums ]

m = map(int, str_nums)

numbers = [-1, -2, -3, -4]

p_numbers = [ abs(item) for item in numbers ]

m = map(abs, numbers)

def quadratic_equation(a, b):
    return a ** 2 + b ** 2 + 2 * a * b

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 0]

q_numbers = [ quadratic_equation(n1, n2)  for n1, n2 in zip(x, y) ]

# without using "for" loop
m = map(quadratic_equation, x, y)

from math import factorial
numbers = [1, 2, 3, 4, 5]

fact = [ factorial(number) for number in numbers ]

# using map
m = map(factorial, numbers)


def square_number(number):
    return number ** 2

class Squares:
    def __call__(self, number):
        return number ** 2

s = Squares()

m = map(s, numbers)  # s(1), s(2), s(3), s(4), s(5)