# dictionary comprehension
sentence = "this is a bunch of words"
# o/p = {"this": 4, "is": 2, "a": 1, "bunch": 5, "of": 2, "words": 5}

words = sentence.split()
word_count = { }
for word in words:
    word_count[word] = len(word)    # word_count['this'] = 4

# using dict comprehension
_words_count = { word: len(word) for word in words }

sentence = "hello world welcome to python hello hi world welcome to python"
# {"hello": 2, "world": 2..}
words = sentence.split()
word_count = { }
for word in words:
    word_count[word] = words.count(word)

# using dict comprehension
_word_count = { word: words.count(word)  for word in words }

word = "abcdABCD"
word_ascii_pair = { }

for letter in word:
    word_ascii_pair[letter] = ord(letter)

# using comprehension
_word_ascii_pair = {  letter: ord(letter) for letter in word }

buildings = {
                'burj khalifa':                     828,
                'Shanghai_Tower':                   632,
                'Abraj_Al_Bait_Clock Tower':        601,
                'Ping_An_Finance_Centre_Shenzhen':  599,
                'Lotte World Tower':                554.5,
                'World Trade Center':               541.3
                }

# 1 meter == 3.28 feets
buildings_feets = { }
for building, height in buildings.items():
    buildings_feets[building] = height * 3.28

# using comprehension
_building_feets = { building: height * 3.28  for building, height in buildings.items() }

cities = ['Tokyo',
          'Delhi',
          'Shanghai',
          'Sao Paulo',
          'Mumbai'
          ]
population = ['38,001,000',
              '25,703,168',
              '23,740,778',
              '21,066,245',
              '21,042,538'
              ]

city_population_pair = { }

for city, _population in zip(cities, population):
    city_population_pair[city] = _population

# using comprehension
_city_population_pair = { city: _population  for city, _population in zip(cities, population)}

dial_codes = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
    ]
# {'India': 91, 'Japan': 81 ....}
country_telephone_code = { }

for item in dial_codes:     # for code, country in dial_codes
    code, country = item        # code = item[0], country= item[1]
    country_telephone_code[country] = code

# using comprehension
_country_code_pair = {  country: code for code, country in dial_codes }

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# {'AAPL': 612.78, 'IBM': 205.55}

price_more_200 = { }

for name, price in prices.items():
    if price > 200:
        price_more_200[name] = price

# using comprehesion
_price_more_200 = { name: price for name, price in prices.items() if price > 200 }

# set comprehension
nums = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
# list comprehension
squares = [ number ** 2  for number in nums ]
_squares = { number ** 2  for number in nums }