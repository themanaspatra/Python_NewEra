# Write a program to get the below output
sentence = "hello world welcome to python programming hi there"
# o/p: d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }"
d = {}

for ele in sentence.split():
    if ele[0] not in d:
        d[ele[0]] = [ele]
    else:
        d[ele[0]] += [ele]

print(d)

from collections import defaultdict

out = defaultdict(list)
for ele in sentence.split():
    out[ele[0]] += [ele]
print(out)

# Reverse the values in the dictionary if the value is of type String
d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

for key, value in d.items():
    if isinstance(value, str):
        d[key] = value[::-1]

print(d)

# Program to print the number of occurrences of characters in a String without using inbuilt functions.
s = 'helloworld'

print({ele: s.count(ele) for ele in s})

# Program to print only the repeated characters and count of the same.
s = 'helloworld'

print({ele: s.count(ele) for ele in s if s.count(ele) > 1})

# Write a program to replace value present in nested dictionary.
d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# Replace ""nose"" with ""net"""
d['b']['n'] = "net"
print(d)

# Write a program to count the number occurrences of each item in the list without using any inbuilt functions
names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']

print({name: names.count(name) for name in names})

# Write a program to find most common words in a given list.
words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes',
         'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look',
         'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under']
from collections import Counter
word_common = Counter(words)
print(word_common.most_common(1))

common_word = {word: words.count(word) for word in words}
*others, most_common = sorted(common_word.items(), key=lambda item: item[-1])
print(most_common)

# Write a program to get all the duplicate items and the number of times the item is repeated in the list.
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']

print({name: names.count(name) for name in names if names.count(name) > 1})

# Write a program to map a product to a company and build a dictionary with company and list of products pair
all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows', 'iOS', 'Google Drive', 'One Drive']

# Pre-defined products for different companies
apple_products = {'iPhone', 'Mac', 'iWatch'}
google_products = {'Gmail', 'Maps', 'Google Drive'}
msft_products = {'Windows', 'One Drive'}

from collections import defaultdict
d = defaultdict(list)

for product in apple_products:
    if product in apple_products:
        d["apple"] += [product]
    if product in google_products:
        d["google"] += [product]
    if product in msft_products:
        d["microsoft"] += [product]

print(d)

# Grouping Flowers and Animals in the below list
items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']

group = {}

for item in items:
    ele, typp = item.split("-")
    if typp == "flower":
        if typp not in group:
            group["flower"] = [ele]
        else:
            group["flower"] += [ele]
    elif typp == "animal":
        if typp not in group:
            group["animal"] = [ele]
        else:
            group["animal"] += [ele]
print(group)

d = {}
for item in items:
    ele, typp = item.split("-")
    if typp not in d:
        d[typp] = [ele]
    else:
        d[typp] += [ele]
print(d)

# Grouping files with same extensions
files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
exten = defaultdict(list)
for file in files:
    if file[-3:] == "txt":
        exten["txt"] += [file]
    elif file[-3:] == "pdf":
        exten["pdf"] += [file]

print(exten)

d = {}
temp = ''
for file in files:
    temp = file.split('.')[-1]
    if temp not in d:
        d[temp] = [file]
    else:
        d[temp] += [file]
print(d)

# Count number of words in a sentence in the form of dictionary. ignore special characters.
sentence = "Hi there! How are you:) How are you doing today!"

print({ele: sentence.count(ele) for ele in sentence.split()})

# Grouping even and odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # o/p should be {1: [1, 3, 5, 7, 9], 0: [2, 4, 6, 8, 10]}"

group = defaultdict(list)
for no in numbers:
    if no % 2 == 0:
        group[0] += [no]
    else:
        group[1] += [no]

print(group)

# Write a program to get the indices of each item in the below list
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# output should be -  {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}"

d = {}
for index, value in enumerate(names):
    if value not in d:
        d[value] = [index]
    else:
        d[value] += [index]
print(d)


# Comprehensions
# ---------------
# Building a dict of word and length pair
words = "This is a bunch of words"

print({word: len(word) for word in words.split()})

# Flipping keys and values of the dictionary using dict comprehension
d = {'a': 1, 'b': 2, 'c': 3}

print({value: key for key, value in d.items()})

# Counting the number of each character in a String
my_string = 'guido van rossum'

print({ele: my_string.count(ele) for ele in my_string})

# Counting the number of each character in a String
sentence = "hello world welcome to python hello hi world welcome to python"

print({ele: sentence.count(ele) for ele in sentence})

# Dictionary of character and ascii value pairs
s = 'abcABC'

print({ele: ord(ele) for ele in s})

# Creating Dictionary of city and population pairs using Dict Comprehension
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

print({city: popul for city, popul in zip(cities, population)})

# Create a dictionary of dialcode and country from the following list
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

print({dial: con for dial, con in dial_codes})

# Building a dictionary whose price value is more than 200
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

print({com: price for com, price in prices.items() if price > 200})
