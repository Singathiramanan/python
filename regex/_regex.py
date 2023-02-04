from re import findall, sub, finditer

sentence = "the theory of relativity"

matches = findall(r"the", sentence)

matches = findall(r"cat", "the dragging belly indicates your cat is too fat")

matches = findall(r"python", "python and java are object oriented languages")

matches = findall(r"aeiou", "hello how are you doing anna")

matches = findall(r"aeiou", "hello how are you doing anna, aeiou and hi")

matches = findall(r"[Ss]mith", "hello smith how are you doing. Smith thanks")

matches = findall(r"sep[ae]rate", "they got a seperate house last year")

matches = findall(r"[aeiou]", "hello world welcome hello anna i have you elephant")

matches = findall(r"hello", "hello world welcome hello anna i have you elephant hello there")

matches = findall(r"[abcd]", "hello world welcome abcd hi")

matches = findall(r"[0123456789]", "the cost this book is Rs.100 and the cost of other book is Rs145")

matches = findall(r"[0-9]", "the cost this book is Rs.100 and the cost of other book is Rs145")

matches = findall(r"<h[1-6]>", "<h7> welcome to Python </h1>")

matches = findall(r"[a-z]", "hello HOW ARE You hi there HEY THERE BAngalore")

matches = findall(r"[A-Z]", "hello HOW ARE You hi there HEY THERE BAngalore")

matches = findall(r"\d", "the cost this book is Rs.100 and the cost of other book is Rs145")

matches = findall(r"\s", "hello world welcome to python hi there how are you")

# d = {'h': 10, 'e': 12, 'H': 5}
matches = findall(r'[a-zA-Z]', "hello! there HEL23LO hello T88here Hi Hello How are You how are you")

# using normal dictionary
letter_count_pair = { }
for letter in matches:
    if letter in letter_count_pair:
        letter_count_pair[letter] = letter_count_pair[letter] + 1
    else:
        letter_count_pair[letter] = 1

# using defaultdict
from collections import defaultdict
_letter_count_pair = defaultdict(int)
for letter in matches:
    _letter_count_pair[letter] += 1

# using dictionary comprehension
letter_count_pair_ = { letter: matches.count(letter) for letter in matches }

# "+" matches with one or more occurances of previous expression
matches = findall(r"[0-9]+", "cost of iphone is $12.23 $2500 the cost of the book is Rs.100 and the cost of the other is 1599 rupees")
# matches = findall(r"\d+", "the cost of the book is Rs.100 and the cost of the other is 1599 rupees")

matches = findall(r"[abcd]+", "abcdefg hijkab")

matches = findall(r"an+a", "hello annnnnnnnnnnnnnnnnnnnnnnna hi there")

matches = findall(r"[a-zA-Z]+", "hi there! how are YOu doing! my email address is spam@company.com")

word = "hello456world987 welcome to py345thon hi prog74563854mming"
# 4 + 5 + 6 + 9 + 8 + 7 + 3 + 4 + 5 + 7 + 4 + 5 + 6 + 3 + 8 + 5 + 4
# 456 + 987 + 345 + 74563854

digits = findall(r"[0-9]", word)

# numbers = [ int(digit) for digit in digits ]
total = 0
for digit in digits:
    total += int(digit)

whole_numbers = findall(r"[0-9]+", word)

_total = 0
for number in whole_numbers:
    _total += int(number)

message = "Downloading file archive.zip to downloads folder..."
message = "Downloading file sample.log to downloads folder..."
message = "Downloading file image.png to downloads folder..."
message = "Downloading file index.xhtml to downloads folder..."

matches = findall(r"[a-z]+\.[a-z]+", message)

# ? zero or max one occurance of previous expression
matches = findall(r"colou?r", "what colour do you like")

matches = findall(r"https?://", "https://www.google.com")

matches = findall(r"July?", "Jul the 26th day")

matches = findall(r"an+a", "aa")

matches = findall(r"an*a", "annnnnnnnnna")

matches = findall(r'Inbox\(?\d*\)?', "Inbox(10)")

matches = findall(r"[^0-9]", "the cost of the book is Rs.100!")

# carret symbol inside charater set is called negation
matches = findall(r"[^abcd]", "abcdefg hicjklmd hello123, Hi! AB")

matches = findall(r"[^0-9]", "the cost of the book is Rs.100!")

matches = findall(r"[^0-5]", "the cost of the book is Rs.100! and 500 and 7897")

sentence = "@hello world123 hi there welcome1234"
# output
# new_sentence = "@hello world hi there welcome"
matches = findall(r"[^0-9]", sentence)
new_sentence = "".join(matches)

word = "hello@world!!! welcome!! to Python$# python234234 & jav232a are object oriented!!!"

matches = findall(r"[^a-zA-Z0-9\s]", word)
# print(f"Total number of special characters {len(matches)}")

# if the carret symbol is outside the character-set, the meaning of it is begining of the string
# or try to match the pattern at the begning of the string
matches = findall(r"^hello", "hi hello world hello there hello")

matches = findall(r"hello$", "hi hello world hello there hello")

matches = findall(r"^hello$", "hello")

def udp_lines():
    with open("../data_files/sample.log", "r") as f:
        for line_no, line in enumerate(f, start=1):
            matches = findall(r"UDP$", line)
            if matches:     # checking if there is a match or finall returned a list with # atleast one item
                print(line_no, line.strip())

sentence = "what a beautiful day today is"
# pattern should start with a word character
# \b is called as word boundary
# any transition bettwen a non word character and a word character or vice-versa
# it is called as "word boundary"
matches = findall(r"\bday", sentence)

# should end with word boundary
matches = findall(r"day\b", sentence)

# should start with word boundary and end with word boundary
matches = findall(r"\bday\b", sentence)

sentence = 'hello world hi hello universe how are you happy birthday h1b'

# using regex
matches = findall(r"\bh[a-zA-Z0-9]+", sentence)

# without usign regex
starts_h = [ ]
for word in sentence.split():
    if word.startswith('h'):        # word[0] == 'h'
        starts_h.append(word)

sentence = 'Python is a Programming language. Python is easier than Java helloPython'

matches = findall(r"\b[PJ][a-zA-Z0-9_]+", sentence)

sentence = 'hello world hi hello universe how are you happy birthday feeling very sleepy flying'

matches = findall(r"[a-zA-Z0-9_]+y\b", sentence)

words_ends_y = [ ]
for word in sentence.split():
    if word[-1] == "y":
        words_ends_y.append(word)

sentence = "hello hi american engieers and indians united states Americans U18 iMAC"

# without using regular expression
vowel_words = [ ]
for word in sentence.split():
    if word[0] in "aeiouAEIOU":
        vowel_words.append(word)

# using regular expression
matches = findall(r"\b[aeiouAEIOU][a-zA-Z0-9_]+", sentence)

sentence = "This is PYTHON programming LANGUAGE and REGEX SOMEthing"

# Matches only upper case words
matches = findall(r"\b[A-Z]+\b", sentence)

# matches only lower case word
matches = findall(r"\b[a-z]+\b", sentence)

sentence = "downloading apple.pdf to downloads folder and apple.doc and google.txt and google.pdf microsoft.xls"

matches = findall(r"\b[a-zA-Z]+\.pdf\b", sentence)

# matches only question marks
matches = findall(r"\?", "how are you? how old are you? wherwe were you?")

sentence = "hello hi how are you what is your name he is older than me how old are you"

# matches only 3 character words
matches = findall(r"\b[a-zA-Z]{2}\b", sentence)

sentence = "Copyright 1998. All rights reserved ph.No. 12345456676"

# trying to match exactly 4 digits pattern (1998)
matches = findall(r"\b\d{4}\b", sentence)

# 876-645-5678
sentence = "the telephone number is 234-0956-7564 and pincode is 560001"

matches = findall(r"\d{3}-\d{3}-\d{4}", sentence)

# match only 800 and 900 numbers
# 800-746-0987
# 900-654-9087
# 100-098-0987
sentence = "the telephone number is 700-956-7564 and pincode is 560001"

matches = findall(r"[89]00-\d{3}-\d{4}", sentence)

sentence = "the telephone number is some id is INDBLR875293485 and pincode is 560001 and "

matches = findall(r"\b\d{6}\b", sentence)

sentence = "he helps the community and he is the hero of the day"

matches = findall(r"\bhe[a-zA-Z0-9_]*", sentence)

sentence = "my pan number is ABCDE1234X and the other number is XYZTR3104J id is 123XYZTR3104J89"

matches = findall(r"\b[A-Z]{5}\d{4}[A-Z]{1}\b", sentence)


sentence = "I am travelling from BLR to DEL tomorrow BANGALORE and DELHI and two cities in india"

matches = findall(r"\b[A-Z]{3}\b", sentence)

line = "03/22 08:51:06 WARNING :.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available."

# matches all upper case characters (induvidual characters)
matches = findall(r"[A-Z]", line)

# matches all upper case letter pattern
matches = findall(r"[A-Z]+", line)

matches = findall(r"\b[A-Z]+", line)

line = "03/22 08:51:06 WARNING :.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available."
matches = findall(r"[A-Z]+\b", line)

def upper_case_words():
    upper_words = [ ]
    with open("../data_files/sample.log") as f:
        for line in f:
            matches = findall(r"\b[A-Z]+\b", line)
            if matches:
                for match in matches:
                    upper_words.append(match)
        return upper_words

# line = "03/22 08:51:01 INFO   :.main: *************** RSVP Agent started ***************"
def count_spaces():
    count = 0
    with open("../data_files/sample.log") as f:
        for line in f:
            matches = findall(r"\s", line)
            if matches:
                count = count + len(matches)
    return count

def count_upper_case_words():
    count = 0
    with open("../data_files/sample.log") as f:
        with open("./ucase.txt", 'w') as fw:
            for line in f:
                matches = findall(r"\b[A-Z]+\b", line)
                if matches:
                    fw.write(",".join(matches))
                    fw.write("\n")
                    count = count + len(matches)
    return count

def count_upper_case_letters():
    """ Function that counts the number of upper case characters in the file"""
    count = 0
    with open("../data_files/sample.log") as f:
        for line in f:
            matches = findall(r"[A-Z]", line)
            if matches:     # checking if the list has atleast one item  
                count = count + len(matches)
    return count

def count_words():
    """Returns total words in the file"""
    count = 0
    with open("../data_files/sample.log") as f:
        for line in f:
            matches = findall(r"\b[a-zA-Z]\w+\b", line)
            if matches:
                count = count + len(matches)
    return count

def vowels_count():
    """Counts total number of vowel letters in the file"""
    count = 0
    with open("../data_files/sample.log") as f:
        for line in f:
            matches = findall(r"[aeiouAEIOU]", line)
            if matches:
                count = count + len(matches)
    return count

sentence = "python and java are object oriented prgoramming languages"

matches = findall(r"(python|java)", sentence)


def time_stamps():
    with open("../data_files/sample.log") as f:
        for line in f:
            matches = findall(r"\b(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]\b", line)
            if matches:
                print(matches)

# Matches valid year (YYYY-MM-DD)
matches = findall(r"\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])", "2021-12-31")

# using regular expression
def get_log_lines():
    with open("../data_files/sample.log") as f:
        for line in f:
            matches = findall(r"(?:0[1-9]|1[0-2])/98", line)
            if matches:
                print(line, end="")

# without using regex
def get_lines():
    with open("../data_files/sample.log") as f:
        for line in f:
            if line.strip():
                words = line.split()
                if words[0].split("/")[-1] == "98":
                    print(line, end="")

# # string method
# new_sentence = sentence.replace(" ", "\n")
    
sentence = "hello world welcome to python"

# using regex
new_sentence = sub(r'\s', "\n", sentence)

new_sentence = sub(r"python", "ruby", sentence)

sentence = "hello world welcome to python"

new_sentence = sub(r"[aeiou]", "*", sentence)

sentence = "hel45lo wor2ld wel32come to p334yt5hon"

new_sentence = sub(r"\d", "*", sentence)

sentence = "#hel45lo wor2ld wel32com%$#e t!!!o p334yt5ho#@n"

new_sentence = sub(r"[^a-zA-Z0-9_\s]", "S", sentence)

sentence = "java and Python are programming languages and html and css are markup languages"

new_sentence = sub(r"and", "&", sentence)

def replace_java_with_python():
    with open('../data_files/java.txt') as java:
        with open('python.txt', 'w') as py:
            for line in java:
                py_line = sub(r"java", "python", line)
                py.write(py_line)

sentence = "        this    is     a    string                         "

def _lstrip(line):
    """Removes trailing whitespaces and returns a new string"""
    return sub(r"^\s+", "", line)

def _rstrip(line):
    """Removes leading whitespaces and returns a new string"""
    return sub(r"\s+$", "", line)

def _strip(line):
    """Removes trailing and leading whitespaces and returns a new string"""
    return sub(r"(^\s+ | \s+$)", "", line)


sentence = "42634238 this is a 3242343 string with traili734857384ng and leading numbers 9089798"

numbers_begining = findall(r"^\d+", sentence)
numbers_ending = findall(r"\d+$", sentence)

s_begining = numbers_begining[0]
s_ending = numbers_ending[0]

print(len(s_begining))
print(len(s_ending))


sentence = "        this    is     a    string                         "

def get_leading_trailing_spaces(line):
    spaces_begining = findall(r"^\s+", line)
    spaces_ending = findall(r"\s+$", line)

    count_spaces_begining = len(spaces_begining[0])
    count_spaces_ending = len(spaces_ending[0])
    return (count_spaces_ending, count_spaces_begining)


sentence = "hello world welcome hello there hello there hello universe"

matches = finditer(r"hello", sentence)
_matches = findall(r"hello", sentence)

# list of tuples with each tuple with start and end index of occurances of "hello"
indexes = [ (item.start(), item.end()) for item in matches]