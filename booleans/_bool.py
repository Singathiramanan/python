# words = ['apple', 'google', 'gmail', 'yahoo']
words = [ ]

if len(words) > 0:      # if the length of the list is greater than zero
    # you are checking if the list has atleast one item
    # we want to loop through the list if the list has atleast one item in it
    for word in words:
        print(word)
else:
    print("the list is empty")

# i am checking the boolean value of the list "words"
# i am checking if the list evaluates to True or False
if words:       #  len(words) > 0
    for word in words:
        print(word)
else:
    print("the list is empty")


if len(line) > 0:       # checking if the string has atleast one character
    words = line.split()
    print(words[0])
else:
    print("Got an empty string")
line = "         hello world                 "
clean_line = line.strip()
if clean_line:            # len(line) > 0
    words = clean_line.split()
    print(words[0])
else:
    print("Got an empty string")
