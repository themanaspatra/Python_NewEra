# Print numbers from 0 to 4 (upto 5 but not including 5)
for no in range(5):
    print(no, end='\t')

print()
# Print numbers from 1 to 4 (num starts from zero if start index is omitted)
for no in range(1, 5):
    print(no, end='\t')

print()
# Print every alternate numbers starting zero
for no in range(0,50,2):
    print(no, end='\t')

print()
# Print number from 10 to 1
for no in range(10,0,-1):
    print(no, end='\t')

print()
# Print number form 10 to 0
for no in range(10,-1,-1):
    print(no, end='\t')

print()
# Print alternate numbers from 10 to 0.
for no in range(10,-1,-2):
    print(no, end='\t')

print()
# Print "Python is awesome!!" 5 times
for _ in range(5):
    print("Python is awesome!!")

# Print numbers from -10 to -1
for no in range(-10,0):
    print(no, end='\t')

print()
# Print numbers from 10 to -1
for no in range(10, -2, -1):
    print(no, end='\t')

print()
# Print even numbers
for no in range(0,20,2):
    print(no, end='\t')

print()
# Print odd  numbers
for no in range(1,20,2):
    print(no, end='\t')

print()
# Iterate over the list only if the list has atleast 1 item.
l = [[1, 2, 3], [], ["hai"]]
for ele in l:
    if ele:
        print(ele)

# Iterate over the list only if the string has atleast 1 item.

# Iterate over the list only if the dictionary has atleast 1 item.

# Iterate over the list only if the set has atleast 1 item.

# Iterate over the list only if the tuple has atleast 1 item.

# Find the sum of first 10 even numbers
total = 0
for no in range(1, 20, 2):
    total += no
print(total)

# Write a program to print prime numbers from 1 to 50
total = 0


# Write a program for Linear Search


# Program to convert uppercase characters to lowercase characters in the string
string = "HeLLo"
s1 = ''
for ele in string:
    if ele.isupper():
        s1 += chr(ord(ele)+32)
    else:
        s1 += ele
print(s1)

# Program to convert lowercase characters to uppercase characters in the string
string = "HeLLo"
s2 = ''
for ele in string:
    if ele.islower():
        s2 += chr(ord(ele)-32)
    else:
        s2 += ele
print(s2)

# Program to print only integer datatypes in the list
datas = ["hi", "hello", 10, "12.3", 12, 90, 6.2]
for data in datas:
    if isinstance(data, int):
        print(data, end='\t')

print()
# Program to print only integer and float datatypes in the list
datas = ["hi", "hello", 10, "12.3", 12, 90, 6.2]
for data in datas:
    if isinstance(data, (int, float)):
        print(data, end='\t')

print()
# program to print all the numeric values in the list
datas = ["hi", "hello", 10, "12.3", 12, 90, 6.2]
for data in datas:
    if isinstance(data, (int, float)):
        print(data, end='\t')

print()
# Program to print only vowels in the string "Python selenium"
for ele in "Python selenium":
    if ele in "aeiouAEIOU":
        print(ele, end='\t')

print()
# Program to print only consonants in the string "Python selenium"
for ele in "Python selenium":
    if ele not in "aeiouAEIOU":
        print(ele, end='\t')

print()
# Program to print all the square numbers in the list.
nums = [10, 25, 4, 56, 64, 256]
import math
for no in nums:
    temp = math.sqrt(no)
    if no == temp ** 2:
        print(no, end='\t')

print()
# Strings
# ________
# Iterating over string using range function.
s = "hello world"
for ele in range(len(s)):
    print(s[ele], end='\t')

print()
# iterating over a string in reversed direction
for ele in s[::-1]:
    print(ele, end='\t')

print()
# Printing Index and Character using range class
for ele in range(len(s)):
    print(f"{s[ele]} --> {ele}")

# Iterating over multiple string objects using zip class
s1 = "hello"
s2 = "world"
for ele in zip(s1, s2):
    print(ele)

# Printing alternate characters of the string
s1 = "hello world"
for ele in s1[::2]:
    print(ele, end='\t')

print()
# Program to count the number of digits and alphabets in the string "hai 1234 python23"
s = "hai 1234 python23"
alpha_count = 0
digit_count = 0
for ele in s:
    if ele.isalpha():
        alpha_count += 1
    elif ele.isdigit():
        digit_count += 1
print(f"number of digits --> {digit_count}")
print(f"number of alphabet --> {alpha_count}")

# Program to count the number of capital and small letters in the string "HelLo WORld"
s = "HelLo WORld"
upper_count = 0
lower_count = 0
for ele in s:
    if ele.isupper():
        upper_count += 1
    elif ele.islower():
        lower_count += 1
print(f"number of capital letters --> {upper_count}")
print(f"number of small letters --> {lower_count}")

# Lists
# ---------
# Prints the item and its corresponding index in the list
l = [1, 2, 54, 45, 7, 3]
for ele in range(len(l)):
    print(f" {l[ele]}  --> at {ele} index")

# Printing alternate items of the list
for ele in l[::2]:
    print(ele)

# Iterating over multiple lists simultaneously
l1 = [1, 4, 5, 7]
l2 = ['A', 'B', 'C', 'D']
for ele in zip(l1, l2):
    print(ele)

# Iterating through multiple list with un-equal lengths using zip class
from itertools import zip_longest

l1 = [1, 2, 4, 5]
l2 = ['S', 'A', 'C', 'D', 'E']
for ele in zip_longest(l1, l2):
    print(ele)

# Program to print filenames ending with pdf.
files = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.pdf', 'apple.doc']
for file in files:
    if file[-3:] == "pdf":
        print(file)

# Print the extension of each file name in the list
files = ['youtube.txt', 'yahoo.pdf', 'microsoft.doc', 'apple.xls', 'amazon.xml']
for file in files:
    print(file[-3:])

# Program to print the length of each word in the list
for file in files:
    print(f"length of {file} is {len(file)}")

# Program to print the length of each word in the list in th form of tuples
for file in files:
    print((file, len(file)))


# Dictionary
# ------------
# Print only keys of the dictionary
d = {'a': 4, 'b': 5, 'c': 8}
for ele in d.keys():
    print(ele)

# Print Values of the dictionary
for ele in d.values():
    print(ele)

# Print index and item of the dictionary
for index, item in enumerate(d.items()):
    print(f"{item} is at {index} index")

# Count number of words in a sentence using get method
sentence = 'hello world hello world welcome to python'
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

from collections import defaultdict
word_count = defaultdict(int)
for word in words:
    word_count[word] += 1

print(word_count)

from collections import Counter
word_count = Counter(words)
print(word_count)

# Counting number of characters in a string
s = 'abracadabraca'
char_count = {}

for ele in s:
    char_count[ele] = char_count.get(ele, 0) + 1
print(char_count)

from collections import defaultdict
char_count = defaultdict(int)
for ele in s:
    char_count[ele] += 1

print(char_count)

from collections import Counter
char_count = Counter(s)
print(char_count)
print(char_count.most_common())
print(char_count.most_common(1))
print(char_count.most_common()[0])
print(char_count.most_common()[-1])

# Counting number of vowels in a string
s = 'abracadabracaiysuue'
vowels = 'aeiouAEIOU'
vowels_count = {}
for ele in s:
    if ele in vowels:
        vowels_count[ele] = vowels_count.get(ele, 0) +1
print(vowels_count)

# Counting occurances of word in the string
sentence = "hello world welcome to python hello hi hello hello"
occur = {word: sentence.count(word) for word in sentence.split()}
print(occur)

words = sentence.split()
occurs = {}
for word in words:
    occurs[word] = words.count(word)

print(occurs)

occurance = {}
for word in sentence.split():
    occurance[word] = sentence.count(word)

print(occurance)

# Counting occurances of each character in the string
s = 'abracadabraca'
occur = {}
for ele in s:
    occur[ele] = s.count(ele)
print(occur)

occurs = {ele: s.count(ele) for ele in s}
print(occurs)

# Create a dictionary for the below list
cities = [('India', 'Bangalore'),
          ('India', 'Chennai'),
          ('India', 'Delhi'),
          ('India', 'Kolkata'),
          ('USA', 'Dallas'),
          ('USA', 'New York'),
          ('USA', 'Chicago'),
          ('China', 'Beijing'),
          ('China', 'Shanghai')
          ]

print(dict(cities))
city_dict = {}
for city in cities:
    country, citi = city
    if country not in city_dict:
        city_dict[country] = [citi]
    else:
        city_dict[country] += [citi]

print(city_dict)

# Adding items of two lists corresponding to their indices
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
for ele1, ele2 in zip(a, b):
    print((ele1+ele2))

# flattening the list using Multiple "for" loops
items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([ele for item in items for ele in item])

# Python Program for n-th Fibonacci number
a = 0
b = 1
for _ in range(10):
    print(a, end='\t')
    c = a + b
    a = b
    b = c

print()
# Python Program for Sum of squares of first n natural numbers
total = sum(ele ** 2 for ele in range(1, 11))
print(total)

# Python Program for cube sum of first n natural numbers
total = sum(ele for ele in range(1, 11))
print(total ** 3)
