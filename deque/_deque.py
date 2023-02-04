from collections import deque

d = deque(range(10))

sentence = "python is a programming languge"
# o/p "programming languge python is a"

words = sentence.split()

# create a deque object
d = deque(words)
d.rotate(2)
new_sentence = " ".join(d)

# "a programming language python is"
sentence = "python is a programming languge"
words = sentence.split()

d = deque(words)
for _ in range(2):
    temp = d.popleft()
    d.append(temp)

new_string  = " ".join(d)

word = "python"
d = deque(word)
# rotating left
d.rotate(2)

new_word = "".join(d)


word = "python"
d = deque(word)

# rotate characters right
for _ in range(2):
    left_character = d.popleft()
    d.append(left_character)

new_word = "".join(d)


def _rotate(sentence, n=1, direction="left"):
    words = sentence.split()
    if direction == "left":
        for _ in range(n):
            right_most_word =  words.pop()
            words.insert(0, right_most_word)
    elif direction == "right":
        for i in range(n):
            left_most_word = words[i]
            words.remove(words[i])
            words.append(left_most_word)
    return " ".join(words)

def rotate_char(some_string, n=1):
    """this function rotates a the characters of a string from right to left"""
    my_list = list(some_string)
    for _ in range(n):
        right_char = my_list.pop()
        my_list.insert(0, right_char)
    return "".join(my_list)
