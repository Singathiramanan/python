# custom sorting
# ['apple', 'amazon', ... 'zomato']

temperatures = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]
# [("Bangalore", 25), ("Mumbai", 32), ("Delhi", 35), ("Chennai", 37)]

word = "acbdzy"
# "abcdyz"

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }
# {"FB": 10.75, "HPQ": 37.20}

numbers = (1, 2, 6, 7, 10, 3, 4, 5)
# (1, 2, 3, 4, 5, 6, 7, 10)

stocks = [
                {'name': 'IBM', 'shares': 100, 'price': 91.1},
                {'name': 'AAPL', 'shares': 50, 'price': 543.22},
                {'name': 'FB', 'shares': 200, 'price': 21.09},
                {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]
# [
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65},
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
# ]


names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'zomato']


items = ['aaaaaa', 'bbb', 'z', 'yy', 'dd']
# ['z', 'yy', 'dd', 'bbb', 'aaaaa']

def get_len(some_string):
    return len(some_string)

sorted_items = sorted(items, key=get_len)

items = ['bv', 'aw', 'dt', 'cu']
# ['dt', 'cu', 'bv', 'aw']
def get_last_chr(name):
    return name[-1]

by_last_char = sorted(items, key=get_last_chr)

temperatures = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]

def get_temperature(some_tuple):
    return some_tuple[-1]

by_temperature = sorted(temperatures, key=get_temperature)

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }
# {'FB': 10.75, 'HPQ': 37.20}

def get_share_price(some_tuple):
    return some_tuple[-1]

key_value_pair = prices.items()

# list of tuples
by_price = sorted(key_value_pair, key=get_share_price)
# final dictionary
_by_price = dict(by_price)

stocks = [
                {'name': 'IBM', 'shares': 100, 'price': 91.1},
                {'name': 'AAPL', 'shares': 50, 'price': 543.22},
                {'name': 'FB', 'shares': 200, 'price': 21.09},
                {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]

def get_name(some_dict):
    return some_dict['name']

def get_shares(some_dict):
    return some_dict['shares']

def get_price(some_dict):
    return some_dict['price']

by_name = sorted(stocks, key=get_name)
by_shares = sorted(stocks, key=get_shares)
by_price = sorted(stocks, key=get_price)

by_name = sorted(stocks, key=lambda item: item['name'])
by_shares = sorted(stocks, key=lambda item: item['shares'])
by_price = sorted(stocks, key=lambda item: item['price'])

students = [
    {"name": "john", "grade": "A", "age": 26},
    {"name": "jane", "grade": "B", "age": 28},
    {"name": "dave", "grade": "B", "age": 22}
]

def get_student_name(some_student):
    return some_student['name']

def get_student_grade(student):
    return student['grade']

def get_student_age(student):
    return student['age']

by_name = sorted(students, key=get_student_name)
by_grade = sorted(students, key=get_student_grade)
by_age = sorted(students, key=get_student_age)

by_name = sorted(students, key=lambda student: student['name'])
by_grade = sorted(students, key=lambda student: student['grade'])
by_age = sorted(students, key=lambda student: student['age'])

sentence = "this is a programming language and programming is fun"
words = sentence.split()
word_len_pair = { word: len(word)  for word in words }

def get_word_len(some_tuple):
    return some_tuple[-1]

# sort the dictioanry
by_len = sorted(word_len_pair.items(), key=lambda item: item[-1])
by_len = sorted(word_len_pair.items(), key=get_word_len)

sentence = "this is a programming language and programming is fun"

words = sentence.split()
word_len_pair= { word: len(word) for word in words if words.count(word) == 1}
by_len = sorted(word_len_pair.items(), key=lambda item: item[-1])


word = "hi hello hi hi hi iiii"

char_count_pair = { letter: word.count(letter)  for letter in word }

most_repeated_letter = sorted(char_count_pair.items(), key=lambda item: item[-1])