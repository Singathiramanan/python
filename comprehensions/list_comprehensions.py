numbers = [1, 2, 3, 4, 5]
squares = [ ]
for number in numbers:
    squares.append(number ** 2)

# List Comprehension # general syntax of list comprehension
# [ expression   for item in some_iterable ]
_squares = [ number ** 2  for number in numbers ]

evens = [ ]
for i in range(0, 51):
    if i % 2 == 0:
        evens.append(i)

# using comprehension
_evens = [ i for i in range(51) if i % 2 == 0 ]

# i want list of strings that starts with vowel character
names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
vowels = [ ]
for name in names:
    if name[0] in "aeiou":  # ['a', 'e', 'i', 'o', 'u'] or ('a', 'e', 'i', 'o', 'u')
        vowels.append(name)

# using comprehension (Pythonic way or pythonic code)
_vowels = [ name  for name in names if name[0] in "aeiou" ]

languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']
p_languages = [ ]

for language in languages:
    if language[0] == 'P':
        p_languages.append(language)

# using comprehension
_p_languages = [ language  for language in languages if language[0] == 'P' ]


names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']

names_consonents = [ ]
for name in names:
    if name[0] not in "aeiou":
        names_consonents.append(name)

# using comprehension
_names_consonents = [ name  for name in names if name[0] not in "aeiou" ]

names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

# [("apple", 5), ("google", 6), ("yahoo", 5), ("facebook", 8) ...]

str_len_pair = [ ]
for name in names:
    str_len_pair.append((name, len(name)))

# using comprehension
_str_len_pair = [ (name, len(name))   for name in names ]

names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
less_6_chars = [ ] 
for name in names:
    if len(name) < 6:
        less_6_chars.append(name)

# using list comprehension
_less_6_chars = [  (name, len(name)) for name in names if len(name) < 6 ]
# # different ways of getting index and item 
# for item in enumerate(numbers):     # item is a tuple
#     index, name = item      # tuple unpacking

# for item in enumerate(numbers):
#     index = item[0] # tuple indexing
#     name = item[1]



# for i in range(0, len(names)):
#     print(i, name)

numbers = [1, 2, 3, 4, 5]
index_item = []

for index, item in enumerate(numbers):
    index_item.append(item ** index)

# using comprehension
_index_item = [  item ** index for index, item in enumerate(numbers) ]

numbers = [1, 2, 3, 4, 5]

_fact = [ ]
from math import factorial
from re import S
for number in numbers:
    _fact.append(factorial(number))

# using comprehension
__fact = [ factorial(number) for number in numbers ]

names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

even_items = [ ]
for name in names:
    if len(name) % 2 == 0:
        even_items.append(name[::-1])
    else:
        even_items.append(name)

def reverse_even_item(name):
    if len(name) % 2 == 0:
        return name[::-1]
    else:
        return name

# using comprehension
_even_items = [ name[::-1]  if len(name) % 2 == 0 else name for name in names  ]

_even_items = [ reverse_even_item(name) for name in names  ]

# reverse only those items which are of type str
data = ['hello', 123, 1.2, 'world', True, 'python']
# ['olleh', 123, 1.2, 'dlrow', True, 'nohtyp']
# without using list comprehension
reversed_data = [ ]
for item in data:
    if isinstance(item, str):
        reversed_data.append(item[::-1])
    else:
        reversed_data.append(item)
# --------------------------------------------------
# using list comprehension
def spam(item):
    if isinstance(item, str):
        return item[::-1]
    return item

r_data = [ spam(item) for item in data ]
# --------------------------------------------------

# list of prime numbers from 1-50
def is_prime(number):
    for i in range(2, number):  # i in range(2, 17)
        # the control will enter if condition only if the number is 
        # divisible by i
        if number % i == 0:
            return False
    return True

# without using comprehension
prime_numbers = [ ]
for i in range(1, 51):
    if is_prime(i):     # if is_prime(i) == True
        prime_numbers.append(i)

_prime_numbers = [ i  for i in range(1, 51) if is_prime(i) ]

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
# total = [6, 8, 10, 12]
total = [ ]

for item in zip(a, b):
    first_number, second_number = item      # tuple unpacking
    total.append(first_number + second_number)

# standard practice
for first_number, second_number in zip(a, b):
    total.append(first_number + second_number)

# using comprehesion
_total = [ fnumber + snumber for fnumber, snumber in zip(a, b) ]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
flat_list = [ ]
for item in matrix:
    for number in item:
        flat_list.append(number)

# alternate solution
for item in matrix:
    flat_list.extend(item)

# using comprehension
_flat_list = [ number for item in matrix for number in item]

letters = "ABCDEFGH"
numbers = [0, 1, 2, 3, 4, 5, 6, 7]

# [A0, B1, C2, D3 ...]
pairs = [ ]
for letter, number in zip(letters, numbers):
    pairs.append(letter + str(number))

# using comprehension
_pairs = [  letter + str(number)  for letter, number in zip(letters, numbers) ]