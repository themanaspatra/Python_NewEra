# **1. Write a program to find the length of the string without using inbuilt function (len)**
print("Q.01")
s = "awesome"
count = 0
for _ in s:
    count += 1
print(f"the len of given string is  {count}")

print()
# **2. Write a program to reverse a string without using any inbuilt functions.**
print("Q.02")
string = "hello world"
s_ = ''
for ele in string:
    s_ = ele + s_
print(f"the reverse of given string is {s_}")

_s = ""
for ele in string[::-1]:
    _s += ele
print(f"the reverse of given string is {_s}")

print()
# **3. Write a program to replace one string with another. e.g. "Hello World" replaces "World" with "Universe".**
print("Q.03")
string = "Hello World"
s = string.replace("World", "Universe")
print(s)

s_ = ""
for ele in string.split():
    if ele == "world":
        s_ += "Universe"
    else:
        s_ += ele
print(s)

print()
# **4. How to convert a string to a list and vice-versa.**
print("Q.04")
string = "hello world"
list_string = string.split()
print(list_string)
print(" ".join(list_string))

print()
# **5. Convert the string "Hello welcome to Python" to a comma separated string.**
print("Q.05")
string = "Hello welcome to Python"
list_string = string.split()
print(",".join(list_string))

print()
# **6. Write a program to print alternate characters in a string.**
print("Q.06")
s = "awesome"
print(s[::2])

print()
# **7. Write a Program to print ascii values of the characters present in a string.**
print("Q.07")
s = "awesome"
for ele in s:
    print(f"ASCII value of {ele} is --> {ord(ele)}")

print()
# **8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.**
print("Q.08")
s = "Hello World"
new = ""
for ele in s:
    if ord('A') <= ord(ele) <= ord('Z'):
        new += chr(ord(ele)+32)
    elif ord('a') <= ord(ele) <= ord('z'):
        new += chr(ord(ele)-32)
print(new)

print()
# **9. Write a program to swap two numbers without using the 3rd variable.**
print("Q.09")
a = 5
b = 10
a, b = b, a
print(a, b)

print()
# **10. Write a program to merge two different lists.**
print("Q.10")
l1 = [1, 5, 7, 3]
l2 = [9, 7, 6, 2]
print(l1+l2)
print([*l1, *l2])

print()
# **11. Write a program to read a random line in a file. (ex. 50, 65, 78th line)**
print("Q.11")


def read_line(line_wanted):
    with open(r"C:\Users\Lenovo\Desktop\NewEra\practice\extra_files\sample.txt", 'r') as f:
        for lineno, line in enumerate(f, start=1):
            if line_wanted == lineno:
                print(line)


read_line(2)

print()
# **12. Write a program to read random lines in a file. (ex. I want read all lines 10th to 15th line)**
print("Q.12")
from itertools import islice


def read_random(start_line, last_line):
    with open(r"C:\Users\Lenovo\Desktop\NewEra\practice\extra_files\sample.txt", 'r') as f:
        read = islice(f, start_line-1, last_line)
        for line in read:
            print(line)


read_random(2, 5)

print()
# **13 Program to print the last "N" lines of a file.**
print("Q.13")
from collections import deque


def read_last_line(fetch_line):
    with open(r"C:\Users\Lenovo\Desktop\NewEra\practice\extra_files\sample.txt", 'r') as f:
        read = deque(f, fetch_line)
    for line in read:
        print(line)


read_last_line(3)

print()
# **14. Write a program to check if the given string is Palindrome or not without using reversed method.**
print("Q.14")


def check_palindrome(string):
    if string == string[::-1]:
        print(f"{string} is palinndrome")


check_palindrome("madam")

print()
# **15 Write a program to search for a character in a given string and return the corresponding index.
print("Q.15")


def search_string(string, search_s):
    for index, ele in enumerate(string):
        if ele == search_s:
            print(f"{search_s} found in {index}")


search_string("awesome", 'o')

print()
# 16. Write a program to get the below output
sentence = "hello world welcome to python programming hi there"
# d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
print("Q.16")
d = {}
for ele in sentence.split():
    if ele[0] not in d:
        d[ele[0]] = [ele]
    else:
        d[ele[0]] += [ele]
print(d)

print()
# **17 Write a program to replace all the characters with - if the character occurs more than once in a string**
my_string = 'hellohai'
# O/P should be '-e--o-ai'
print("Q.17")
s = ''
for ele in my_string:
    if my_string.count(ele) > 1:
        s += '-'
    else:
        s += ele
print(s)

print()
# **18 write a decorator that returns only positive values of subtraction**
print("Q.18")


def positive(func):
    def wrapper(*args, **kwargs):
        from time import time, sleep
        print(f"calling {func.__name__}")
        start = time()
        sleep(1)
        result = func(*args, **kwargs)
        end = time()
        print(f"execution time is: {end-start}")
        return abs(result)
    return wrapper


@positive
def sub(a, b):
    return a - b


print(sub(3, 5))

print()
# **19 How to get the count of the number of instances of a class that is being created.**
print("Q.19")


class Demo:
    COUNT = 0

    def __init__(self):
        Demo.COUNT += 1

    @staticmethod
    def count_instance(demo_instance):
        return Demo.COUNT


d1 = Demo()
d2 = Demo()
d3 = Demo()

demo_instance = [d1, d2, d3]

print(Demo.count_instance(demo_instance))
print(Demo.COUNT)

print()
# **20 Write a function which takes a list of strings and integers.If the item is a string
# it should print as is and if the item is integer or float it should reverse it.**
print("Q.20")


def some_data(some_list):
    empty_list = []
    for ele in some_list:
        if isinstance(ele, str):
            empty_list.append(ele)
        elif isinstance(ele, int):
            empty_list.append(int(str(ele)[::-1]))
        elif isinstance(ele, float):
            empty_list.append(float(str(ele)[::-1]))
    return empty_list


print(some_data([10, 'hello', 5.15, 'hi']))
print()
# **21 Write a class named Simple and it should have iteration capability.**
print("Q.21")


class Simple:

    def __init__(self, a):
        self.a = a

    def __iter__(self):
        return iter(self.a)


s = Simple("hello")
for ele in s:
    print(ele)

print()
# **22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a**
print("Q.22")


class Custom:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __getitem__(self, item):
        return self.__dict__[item]


c = Custom(5, 10)
print(c.a)
print(c['b'])

print()
# **23 Write a python program to get the below output**
print("Q.23")
sentence = "Hi How are you"
# o/p should be "iH woH era uoy"

out = [ele[::-1] for ele in sentence.split()]
print(" ".join(out))

print()
# **24 Write a python program to get the below output**
print("Q.24")
sentence = "Hi How are you"
# o/p should be "ouy era woH iH"


out = [ele[::-1] for ele in sentence.split()[::-1]]
print(" ".join(out))

print()
# **25 Write a lambda function to add two numbers (a, b)**
print("Q.25")


addition = lambda a, b: a + b
print(addition(5, 2))

print()
# **26 What is the output of the following**
print("Q.26")
a = [1, 2, 3]
b = [4, 5, 6]
print([a, b])
print((a, b))

print()
# **27 How to remove duplicates from the list without using inbuilt functions**
print("Q.27")
items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
duplicate = []

for item in items:
    if item not in duplicate:
        duplicate += [item]

print(duplicate)
print(list(set(items)))

print()
# **28 Find the longest word in the sentence**
print("Q.28")
sentence = "Hello world. Welcome to Python"
s = ''
for ele in sentence.split():
    if len(ele) >= len(s):
        s = ele
print(f"longest word i --> {s}")

print()
# **29 write a program to reverse the values in the dictionary if the value is of type String**
print("Q.29")
d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

print({key: value[::-1] if isinstance(value, str) else value for key, value in d.items()})

print()
# **30 write a program to get 1234 from the below tuple
print("Q.30")
t = ('1', '2', '3', '4')
s = ""
for ele in t:
    s += ele
print(int(s))

print()
# **31 How to get the elements that are in list b but not in list a**
print("Q.31")
a = [1, 2, 3]
b = [1, 2, 3, 4]
for ele in b:
    if ele not in a:
        print(ele)

print()
# **32 A function takes variable number of positional arguments as input.
# How to check if the arguments that are passed are more than 5**
print("Q.32")


def func(*args):
    count = 0
    for _ in args:
        count += 1
    if count > 5:
        print(f"more than 5 element passed")


func(1, 4, 2, 'hello', [1], 'hi')


def func(*args):
    if len(*args) > 5:
        print(F"more than 5 argument passed")


func('awesome')

print()
# **33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
print("Q.33")
# # Assume Below is the contents of the log file
#
lines = """CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error
CRITICAL: This is critical"""

with open(r"C:\Users\Lenovo\Desktop\NewEra\practice\extra_files\sample.log", 'r') as f:
    d = {}
    for line in f:
        if line.strip():
            word = line.split()[2]
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1

print(d)

from re import findall

critical_count = findall(r"CRITICAL", lines)
info_count = findall(r"INFO", lines)
error_count = findall(r"ERROR", lines)

print(f"No. of critical lines: {len(critical_count)}")
print(f"No. of info lines: {len(info_count)}")
print(f"No. of error lines: {len(error_count)}")

print()
# **34 Write a function to reverse any iterable without using reverse function.
print("Q.34")


def reverse_func(iterable):
    if isinstance(iterable, (str, list, tuple)):
        return iterable[::-1]
    elif isinstance(iterable, dict):
        some_list = sorted(iterable.items(), reverse=True)
        return dict(some_list)


d1 = "hello"
d2 = [1, 2, 3, 4]
d3 = (1, 2, 3, 4)
d5 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(reverse_func(d1))
print(reverse_func(d2))
print(reverse_func(d3))
print(reverse_func(d5))

print()
# **35 Write a function to print the below output.**
print("Q.35")
# # func("TRACXN", 0)  # Should print RCN
# # func("TRACXN", 1)  # Should print TAX


def func(data, specifier):
    if specifier == 0:
        for ele in data[1::2]:
            print(ele, end="")
        print()
    elif specifier == 1:
        for ele in data[::2]:
            print(ele, end='')
        print()


func("TRACXN", 0)
func("TRACXN", 1)

print()
# **36 Sum all the numbers in the below string.**
print("Q.36")
s = "Sony12India567Pvt2ltd" # eg.1+2+5+6+7+2
total = 0
for ele in s:
    if ele.isdigit():
        total += int(ele)

print(f"total of value is --> {total}")

res = findall(r"\d", s)
print(sum([int(item) for item in res]))

print()
# **37 Write a program to sum all the numbers in below string.**
print("Q.37")
s = "Sony12India567Pvt2ltd"
# eg.12+567+2

res = findall(r"\d+", s)
print(sum([int(item) for item in res]))


print()
# **38 Print all the numbers in the below list**
print("Q.38")
a = ['abc', '123', 'hello', '23']
for ele in a:
    if ele.isdigit():
        print(ele)

print()
# **39 Program to print the number of occurrences of characters in a String without using inbuilt functions.**
print("Q.39")
s = 'helloworld'

print({ele: s.count(ele) for ele in s})

print()
# **40 Program to print only the repeated characters and count of the same.**
print("Q.40")
s = 'helloworld'

print({ele: s.count(ele) for ele in s if s.count(ele) > 1})

print()
# **41 Write a program to get alternate characters of a string in list format.**
print("Q.41")
s = 'helloworld'
l = []
for ele in s[::2]:
    l.append(ele)
print(l)
print([ele for ele in s[::2]])

print()
# **42 Write a program to get square of list of number's using lambda function .**
print("Q.42")
a = [1, 2, 3, 4, 5]
square = lambda no: no ** 2
print(list(map(square, a)))

print()
# **43 Write a function that accepts two strings and returns True if the two strings are anagrams of each other.**
print("Q.43")


def anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        print(f"{str1} and {str2} are anagram")
    else:
        print(f"{str1} and {str2} are not anagram")

anagram("listen", "silent")

print()
# **44 Write a program to iterate through list and build a new list,
# only if the items of the list has even numbers of characters.**
print("Q.44")
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']

print([name for name in names if len(name) % 2 == 0])

print()
# **45 Write a program to iterate through list and build a new dictionary,
# only if the items of the list has even numbers of characters.**
print("Q.45")
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']

print({name: len(name) for name in names if len(name) % 2 == 0})

print()
# **46 Write a program which squares the numbers in a list using map object**
print("Q.46")
a = [1, 2, 3, 4, 5]

print(list(map(lambda ele: ele ** 2, a)))

print()
# **47 Count number of lines in a file without loading the file to the memory**
print("Q.47")
with open(r"C:\Users\Lenovo\Desktop\NewEra\practice\extra_files\sample.txt", 'r') as f:
    count = 0
    for line in f:
        if line.strip():
            count += 1
    print(f"the no. of line in the file are {count}")

print()
# **48 Printing line and line no's in a file**
print("Q.48")
with open(r"C:\Users\Lenovo\Desktop\NewEra\practice\extra_files\sample.txt", 'r') as f:
    for lineno, line in enumerate(f):
        print(lineno, line)

print()
# **49 Write a Program to print the sum of entire list and sum of only internal list**
print("Q.49")
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(sum([ele for item in l for ele in item]))

print()
# **50 Write a program to reverse the list as below**
print("Q.50")
words = ["hi", "hello", "python"]
# res = ["python", "hello", "hi"]

print([word for word in words[::-1]])

print()
# **51 Write a program to update the tuple**
print("Q.51")
t1 = (1, 2, 3, 4)
t2 = (100, 200, 300)
# o/p (1, 2, 3, 4, 100, 200, 300)
print((*t1, *t2))

print()
# **52 Write a program to replace value present in nested dictionary.**
print("Q.52")
d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# # Replace "nose" with "net"
d['b']['n'] = 'net'
print(d)

print()
# **53 Write a program to count the number of white spaces in a file.**
print("Q.53")
with open(r"C:\Users\Lenovo\Desktop\NewEra\practice\extra_files\sample.txt", 'r') as f:
    count = 0
    for line in f:
        res = findall(r"\s", line)
        if res:
            count += len(res)
print(f"no. os whitespace is {count}")

print()
# **54 Grouping anagrams.**
print("Q.54")
l = ["listen", "hello", "eat", "desserts", "silent", "peek", "ate", "keep", "tea", "stressed"]
anagram = {}

for item in l:
    res = "".join(sorted(item))
    if res not in anagram:
        anagram[res] = [item]
    else:
        anagram[res] += [item]
print(anagram)

print()
# **55 What is the difference between defaultdict and normal dictionary.**
#
# **56 Explain property decorator in python.**
#
# **57 What are Mutable and Immutable datatypes.**
#
# **58 Explain get() method in dictionaries.**
#
# **59 Write a list comprehension to get a list of even numbers from 1-50**
print("Q.59")

print([ele for ele in range(1, 51) if ele % 2 == 0])

print()
# **60 Find the longest non-repeated substring in the below string**
print("Q.60")
s = "This is a Programming language and Programming is fun"

longest = max(s.split(), key=len)
print(longest)

print()
# **61 Write a program to find the duplicate elements in the list without using inbuilt functions**
print("Q.61")
names = ['apple', 'google', 'apple', 'yahoo', 'google']
non_dup = []
for name in names:
    if name not in non_dup:
        non_dup.append(name)
print(non_dup)
print(list(set(names)))

print()
# **62 Write a program to count the number occurrences of each item in the list
# without using any inbuilt functions**
print("Q.62")
names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']

print({name: names.count(name) for name in names})

print()
# **63 Write a function to check if the number is Prime**
print("Q.63")


def check_prime(some_num):
    for num in range(2, some_num):
        if some_num % num == 0:
            print(f"{some_num} is not a prime number")
            break
    else:
        print(f"{some_num} is a prime number")


check_prime(5)

print()
# **64 How to create a tuple of numbers from 0 to 10 using range function**
print("Q.64")

print(tuple(range(11)))

print()
# **65 Write a program to find the largest number in the list without using any inbuilt functions**
print("Q.65")
numbers = [10, 20, 30, 40, 50]
max_no = 0

for no in numbers:
    if no > max_no:
        max_no = no
print(f"largest no is {max_no}")

print()
# **66 Write a method that returns the last digit of an integer.
# For example, the call of get_last_digit(3572) should return 2.**
print("Q.66")


def get_last_digit(number):
    return number % 10


print(get_last_digit(3572))

print()
# **67 Write a program to find most common words in a given list.**
print("Q.67")
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
]
d = {word: words.count(word) for word in words}
most, *others = sorted(d.items(), key=lambda item: item[-1], reverse=True)
print(most)

print()
# **68 Make a function named tail that takes a sequence (like a list, string, or tuple)
# and a number n and returns the last n elements from the given sequence, as a list.**
print("Q.68")


def tail(sequence, position):
    if isinstance(sequence, (str, list, tuple)):
        return sequence[-position:]
    return f"Not a sequence"


print(tail([1, 2, 4, 5, 7], 3))

print()
# **69 Write function named is_perfect_square that accepts a number and
# returns True if it's a perfect square and False if it's not.**
print("Q.69")
from math import sqrt


def is_perfect_square(number):
    if int(sqrt(number)) ** 2 == number:
        return True
    else:
        return False


print(is_perfect_square(90))

print()
# **70 Write a program to get all the duplicate items and the number of times the item is repeated in the list.**
print("Q.70")
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']

print({name: names.count(name) for name in names if names.count(name) > 1})

print()
# **71 Write a program to count the number of occurrences of each word in a file.**
print("Q.71")
with open(r"C:\Users\Lenovo\Desktop\NewEra\practice\extra_files\sample.txt", 'r') as f:
    d = {}
    for line in f:
        if line.strip():
            for word in line.split():
                if word not in d:
                    d[word] = 1
                else:
                    d[word] += 1
print(d)

print()
# **72 Write a program to count the number of occurrences of vowels in a file.**
print("q.72")
with open(r"C:\Users\Lenovo\Desktop\NewEra\practice\extra_files\sample.txt", 'r') as f:
    vowel = {}
    for line in f:
        if line.strip():
            for letter in line:
                if letter in "aeiouAEIOU":
                    if letter not in vowel:
                        vowel[letter] = 1
                    else:
                        vowel[letter] += 1
print(vowel)

print()
# **73 Write a program to print all numeric values in a list**
print("Q.73")
items = ['apple', 1.2, 'google', '12.6', 26, '100']

print([item for item in items if isinstance(item, (int, float))])

print()
# **74 Triangle Patterns**
print("Q.74")
# *
# * *
# * * *
# * * * *
# * * * * *

for ele in range(1, 6):
    print('* ' * ele)

print('-' * 50)
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

for ele in range(1, 6):
    print(f'{"* " * ele :>10}')


print('-' * 50)
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

for ele in range(1, 6):
    print(f"{'* ' * ele :^10}")


print('-' * 50)
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for ele in range(6, 0, -1):
    print('* ' * ele)

print('-' * 50)
# * * * * * *
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *

for ele in range(6, 0, -1):
    print(f"{'* ' * ele :>12}")

print('-' * 50)
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

for ele in range(6, 0, -1):
    print(f"{'* ' * ele :^12}")

print('-' * 50)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for row in range(1, 6):
    for ele in range(1, row+1):
        print(ele, end=" ")
    print()

print('-' * 50)
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

print('-' * 50)
#      1
#     1 2
#    1 2 3
#   1 2 3 4
#  1 2 3 4 5
#
#
# **75 Write a program to count the occurrence of a particular word in the file**
print("Q.75")


def extract_word(word):
    with open(r"C:\Users\Lenovo\Desktop\NewEra\practice\extra_files\sample.txt", 'r') as f:
        count = 0
        for line in f:
            if line.strip():
                for ele in line.split():
                    if ele == word:
                        count += 1
    return f"{word} has {count} occurance"


print(extract_word("hello"))


print()
# **76 Write a program to map a product to a company and build a dictionary with company
# and list of products pair**
print("Q.76")
all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows', 'iOS', 'Google Drive', 'One Drive']

# >>> # Pre-defined products for different companies
apple_products = {'iPhone', 'Mac', 'iWatch'}
google_products = {'Gmail', 'Maps', 'Google Drive'}
msft_products = {'Windows', 'One Drive'}
from collections import defaultdict
d = defaultdict(list)
for ele in all_products:
    if ele in apple_products:
        d['apple'] += [ele]
    elif ele in google_products:
        d["google"] += [ele]
    elif ele in msft_products:
        d["msft"] += [ele]

print(d)

print()
# **77 Write a program to rotate items of the list**
print("Q.77")
names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]

print([name for name in names[::-1]])

print()
# **78 Write a program to rotate characters in a string**
print("Q.78")
string = "hello there"

print(string[::-1])

print()
# **79 Write a program to count the number of white spaces in a given string**
print("Q.79")
string = "hello there how are you i am doing good"
count = 0
for ele in string:
    if ele == " ":
        count += 1

print(f"the no of whitespaces are {count}")

from re import findall
res = findall(r"\s", string)
print(f"no of whitespaces are : {len(res)}")

print()
# **80 Write a program to print only non-repeated characters in a string**
print("Q.80")
string = "hello there how r u"
for ele in string:
    if string.count(ele) == 1:
        print(ele)

print()
# **81 What is the difference between a list and a tuple**
#
# **82 Write a program to print all the consonants in a given string**
print("Q.82")
s = 'helloworld'
for ele in s:
    if ele in "aeiouAEIOU":
        print(ele)

print()
# **83 Write a program to count the number of commented lines in a text file**
print("Q.83")
with open(r"C:\Users\Lenovo\Desktop\NewEra\practice\extra_files\sample.txt") as f:
    count = 0
    for line in f:
        if line.strip():
            if line[0] == "#":
                count +=1
print(f"no of comment line are {count}")

print()
# **84 Write a program to check if the year is leap year or not**
print("Q.84")


def check_leap(year):
    if year % 100 == 0:
        print(f"{year} is a leap year")
    elif year % 400 == 0:
        print(f"{year} is a leap year")
    elif year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


check_leap(2024)

print()
# **85 Linear Search**
print("Q.85")

l = [1, 4, 7, 1, 6, 8]


def linear(some_ele):
    for index, value in enumerate(l):
        if value == some_ele:
            print(f"{some_ele} found in {index} index")


linear(7)

print()
# **86 Difference between xrange and range**
#
# **87 Write a program to count no of capital letters in a string**
print("Q.87")
sentence = "Hi How are You WelCome to PytHon"
count = 0
for ele in sentence:
    if ele.isupper():
        count += 1
print(f"the no of capital letter is {count}")

print()
# **88 Write a program to get the below output**
print("Q.88")
# '''
# *
# *
# *
# * *
# *
# * * *
# *
# * * * *
# *
# * * * * *
# '''

for ele in range(1, 6):
    print("*")
    print("* " * ele)

print()
# **89 Write a program to get the below output**
print("Q.89")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# o/p:
# >>> [1, 2]
#     [3, 4]
#     [5, 6]
#     [7, 8]
#     [9]
# ```
for ele in range(0, len(a), 2):
    print(a[ele: ele+2])

print()
# **90 Write a program to check if the elements in the second list is series of continuation
# of the items in the first list**
print("Q.90")

a = [10, 12, 14, 16, 18]
b = [20, 22, 24, 26, 28]
diff = b[0] - a[0]
for ele in range(len(b)):
    if b[ele] - a[ele] != diff:
        print("it is not a sequence")
        break
else:
    print("it is a sequence")

print('-' * 50)
a = [0, 5, 10, 15]
b = [20, 25, 30, 35, 40]
diff = b[0] - a[0]
for ele in range(len(b) - 1):
    if b[ele] - a[ele] != diff:
        print("not a sequence")
        break
else:
    print("it is a sequence")

print('-' * 50)
# x = [10, 20, 30, 40]
# y = [50, 40, 60, 70]

print()
# **91 What is the difference between append() and extend() method in list**
# append() is a method which takes any data type and add it to the list
# extend() is a method which takes only iterables and add it to the list
# **92 Write a program to find the first repeating character in a string**
print("Q.92")
s = "hello world"
for ele in s:
    if s.count(ele) > 1:
        print(f"first repeated character is {ele}")
        break

print()
# **93 Write a program to find the index of nth occurrence of a sub-string in a string**
print("Q.93")
sentence = "hello world welcome to python hello hi how are you hello there"
# >>> index_nth_occurance(sentence, 'hello', 3)
# >>> Start Index: 51, End Index: 56


def occurance(string, sub_string, occur):
    from re import finditer
    matches = finditer(sub_string, string)
    group = [(match.start(), match.end()) for match in matches]
    return group[occur-1]


print(occurance(sentence, "hello", 3))

print()
# **94 Write a program to print prime numbers from 1 to 50**
print("Q.94")


def isprime(number):
    l = []
    for num in range(1, number+1):
        for no in range(2, num):
            if num % no == 0:
                break
        else:
            l.append(num)
    return l


print(isprime(50))

print()
# **95 Write a program to sort a list which has mix of both odd and even numbers,
# the sorted list should have odd numbers first and then even numbers in sorted order**
print("Q.95")
a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
# >>> # o/p should be [1, 3, 7, 9, 11, 2, 4, 6, 8, 12]

odd = [ele for ele in a if ele % 2 == 1]
even = [ele for ele in a if ele % 2 == 0]
odd.sort()
even.sort()
print([*odd, *even])

print()
# **96 Write a program to sort a list which has mix of both odd and even numbers,
# in the sorted list, odd numbers should be in ascending order and even numbers
# should be in descending order**
print("Q.96")
a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
# >>> # o/p should be [1, 3, 7, 9, 11, 12, 8, 6, 4, 2]
odd = [ele for ele in a if ele % 2 == 1]
odd.sort()
even = [ele for ele in a if ele % 2 ==0]
even.sort(reverse=True)
print([*odd, *even])

print()
# **97 Write a program to count the number of occurrences of non-special characters in a given string**
print("Q.97")
s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
from re import findall
res = findall(r"[\w\s]", s)
print(f"no of non- special character is {len(res)}")

print()
# **98 Grouping Flowers and Animals in the below list**
print("Q.98")
items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
group = {}
for item in items:
    entity, type = item.split("-")
    if type not in group:
        group[type] = [entity]
    else:
        group[type] += [entity]
print(group)

print()
# **99 Grouping files with same extensions**
print("Q.99")
files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
extension = {}
for file in files:
    if file[-3:] not in extension:
        extension[file[-3:]] = [file]
    else:
        extension[file[-3:]] += [file]
print(extension)

print()
# **100 Filter only those characters except digits**
print("Q.100")
s = '@hello12world34welcome!123'
s_ = ''
for ele in s:
    if not ele.isdigit():
        s_ += ele
print(s_)
res = findall(r"[^\d]", s)
print("".join(res))

print()
# **101 Count number of words in a sentence. ignore special characters.**
print("Q.101")
sentence = "Hi there! How are you:) How are you doing today!"
print(len(sentence.split()))

print()
# **102 Grouping even and odd numbers**
print("Q.102")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # o/p should be {1: [1, 3, 5, 7, 9], 0: [2, 4, 6, 8, 10]}
group = defaultdict(list)
for no in numbers:
    if no % 2 == 0:
        group['0'] += [no]
    elif no % 2 == 1:
        group['1'] += [no]
print(group)

print()
# **103 Find all max numbers from the below list**
print("Q.103")
numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
temp = max(numbers)
print([num for num in numbers if num >= temp])

print()
# **104 Find all max length words from the below sentence**
print("Q.104")
sentence = "hello world hi apple you yahoo to you"
length_word = max(sentence.split(), key=len)
print([ele for ele in sentence.split() if len(ele) >= len(length_word)])

print()
# **105 Find the range from the following string**
print("Q.105")
sentence = '0-0, 4-8, 20-20, 43-45'
# >>> # Output Should be [0, 4, 5, 6, 7, 8, 20, 43, 44, 45, 46]
l = []
for ele in sentence.split(','):
    ele1, ele2 = ele.split('-')
    if ele1 == ele2:
        l.append(int(ele1))
    else:
        for item in range(int(ele1), int(ele2)+1):
            l.append(item)
print(l)

print()
# **106 Can we override a static method in python?**
# since static method belongs to class but ot the instance of the class i.e. static method cannot
# operates over instance data so they cannot be inherited to the sub class, hence cannot be override
# **107 Write a function which returns the sum of lengths of all the iterables**
print("Q.107")
total_length = ([1, 2, 3], (4, 5), ['apple', 'google', 'yahoo', 'gmail', 'flipkart'],
                {1, 2, 3}, {'a': 1, 'b': 2})
# o/p: 15
count = 0
for item in total_length:
    for _ in item:
        count += 1

print(count)

print()
# **108 Replace whitespaces with newline character in the below string**
print('Q.108')
sentence = "Hello world welcome to python"
from re import sub
res = sub(r"\s", "\n", sentence)
print("".join(res))

print('-' * 50)

s = ""
for ele in sentence:
    if ele == " ":
        s += "\n"
    else:
        s += ele
print(s)

print()
# **109 Replace all vowels with "*"
print("Q.109")
sentence = "hello world welcome to python"
new = ""
for ele in sentence:
    if ele in "aeiouAEIOU":
        new += "*"
    else:
        new += ele
print(new)

print()
# **110 Replace all occurances of "Java" with "Python" in a file**
#
# **111 Maximum sum of 3 numbers and Minimum sum of 3 numbers**
print("Q.111")
numbers = [10, 15, 20, 25, 30, 35, 40, 15, 15]
numbers.sort()
print(numbers)
l1 = sum([ele for ele in numbers[:3]])
l2 = sum([ele for ele in numbers[-3:]])
print(l1)
print(l2)

print()
# **112 Write a program to get the output as below**
print("Q.112")
input = "python@#$%pool"
# # o/p should be ['PYTHON', 'POOL']

res = findall(r"[a-z]+", input)
print([ele.upper() for ele in res])

print()
# **113 Write a program to print all the number which are ending with 5**
print("Q.113")
numbers = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']

print([num for num in numbers if int(num) % 10 == 5])

print()
# **114 Write a program to get the indexes of each item in the below list**
print("Q.114")
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# output should be -  {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}
d = {}
for index, name in enumerate(names):
    if name not in d:
        d[name] = [index]
    else:
        d[name] += [index]
print(d)

print()
# **115 Write a program to print "Bangalore" 10 times without using "for" loop**
print("Q.115")
count = 10
while(count > 0):
    print("Bangalore")
    count -= 1

print()
# **116 Write a program to print all the words which starts with letter 'h' in the given string**
print("Q.116")
string = 'hello world hi hello universe how are you happy birthday'
for ele in string.split():
    if ele.startswith("h"):
        print(ele)

print([ele for ele in string.split() if ele[0] == 'h'])

print()
# **117 Write a program to sum all even numbers in the given string**
print("Q.117")
sentence = 'hello 123 world 567 welcome to 9724 python'

print(sum([int(ele) for ele in sentence if ele.isdigit() and int(ele) % 2 == 0]))

print()
# **118 Write a program to add each number in word1 to number in word2**
print("Q.118")
word1 = 'hello 1 2 3 4 5'
word2 = 'world 5 6 7 8 9'
# # e.g. 1 + 5, 2 + 6, 3 + 7, 4 + 8, 5 + 9
print([int(ele1) + int(ele2) for ele1, ele2 in zip(word1, word2) if ele1.isdigit() and ele2.isdigit()])

print()
# **119 Write a program to filter out even and odd numbers in the given string**
print("Q.119")
sentence = 'hello 123 world 456 welcome to python498675634'
odd = [ele for ele in sentence if ele.isdigit() and int(ele) % 2 == 1]
even = [ele for ele in sentence if ele.isdigit() and int(ele) % 2 == 0]
print(odd)
print(even)

print()
# **120 Write a program to print all the number which are starting with 8**
print("Q.120")
numbers = ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']

print([num for num in numbers if num[0] == '8'])

print()
# 121 Write a program to remove duplicates from the list without using set or empty list
print("Q.121")
l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]
index = 0
while index < len(l1):
    item = l1[index]
    if l1.count(item) != 1:
        l1.remove(item)
    index += 1
print(l1)

print()
# 122 Print all the missing numbers from 1 to 10 in the below list
#
# **123 Write a python program to get the below output**
print("Q.123")
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
# >>> # o/p ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']

print([str(ele1)+ele2 for ele1 in l1 for ele2 in l2])

print()
# 124 Write a python program to get the below output
print("Q.124")
word = "AAAAaaccYYY"
# >>> # o/p ['Y3', 'c2', 'A4', 'a2']
out = []
count = 1
for ele in range(1, len(word)):
    if word[ele] == word[ele - 1]:
        count += 1
    else:
        out.append(word[ele - 1] + str(count))
        count = 1
out.append(word[-1] + str(count))
print(out)

print()
# **125 What is the output of the below function call**
# class Demo:
#     def greet(self):
#         print("hello world")
#
#     def greet(self):
#         print("hello universe")
#
# >>> d = Demo()
# >>> d.greet()
#
# **126 In the list below, find all the number pairs which results in 10 either when added or subtracted**
print("Q.126")
a = [3, 5, -4, 8, 11, 1, -1, 6]
l = []
for ele in a:
    for item in a:
        if ele + item == 10 or ele - item == 10:
            l.append((ele, item))
print(l)

print()
# **127 Write a decorator to prefix +91 to the original phone numbers**
print("Q.127")


def prefix(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return "+91" + res
    return wrapper


@prefix
def phone(number):
    return str(number)


print(phone(7008241393))

print()
# **128 Write a program to get the below output**
print("Q.128")
d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# >>> # o/p should be ['b', 'd']

print([key for key, value in d.items() if value % 2 == 0])

print()
# 129 Can we have multiple __init__ methods in a class
# Yes , we can have multiple __init__ method but the interpreter will always consider the latest one
#
# 130 Why python is Object Oriented?
# Because of its working procedure i.e. python always store the value in the memory and the reference
# i.e. the variable is just pointing to the memory address where the data is store, hence it is an object.
#
# 131 What are .pyc files
# .pyc files are the python class file, we can say bytecodes file which is obtained when the source code
# is executed and the interpreter complied it and give the required output.
#
# 132 Reverse a list without using any built-in functions and slicing
print("Q.132")
l = [4, 5, 1, 7, 3]
l_ = []
for ele in l:
    l_ = [ele] + l_
print(l_)

print()
# 133 Write a program to get the below output
print("Q.133")
input = "10.20.30.40"
#     # o/p = "40.30.20.10"
greet = input.split('.')
greet.sort(reverse=True)
print(".".join(greet))

print()
# 134 What is the difference between while loop and for loop.
#
# While Loop: It is typically used when you want to repeat a block of code until a specific condition is met, and
# you're not sure how many iterations will be needed. The loop continues until the condition becomes false.
#
# For Loop: It is commonly used when you know the number of iterations in advance or when you want to iterate over
# a sequence, such as a list or a range, in a more concise and convenient way.
#
# 135 What are magic methods?
#
# 136 What is pylint.
#
# Pylint is a widely used static code analysis tool for Python. It helps developers identify and fix potential issues,
# maintain coding standards, and improve code quality. Pylint analyzes Python code, checks for errors, and provides
# suggestions and warnings based on a set of predefined coding conventions and best practices.
#
# 137 What is the output of the below program.
print("Q.137")

print([1, 2, 3, 4] * 2)
print((1, 2, 3, 4) * 2)

print()
# 138 What is the difference between the is and == operators
#
# 139 What is "self" in class.
#
# 140 What is assert statement. What is the difference between assert and if/else statement.
#
# The assert statement in Python is used to check if a given condition is true. It is primarily used for debugging and
# testing purposes to verify assumptions about the state of the program. If the condition provided to assert evaluates
# to False, it raises an AssertionError exception, indicating that an unexpected condition has occurred.
#
# In summary, assert statements are primarily used for debugging and testing to validate assumptions, while if/else
# statements are used for conditional execution and program flow control.
#
# 141 What is the difference between a module, a package, and a library
#
# In summary, a module is a single file containing Python code, a package is a directory containing multiple modules
# organized in a hierarchy, and a library is a collection of precompiled modules or packages that provide specific
# functionality. Modules are the smallest unit, packages provide organization and namespaces, and libraries are
# reusable collections of code solving specific problems.

# 142 write a program to get the below output using while loop
print("Q.142")
#            1
#            12
#            123
#            1234

for row in range(1, 5):
    for ele in range(1, row+1):
        print(ele, end="\t")
    print()

print()
# 143 write a program to get the below output
print("Q.143")
items = ['$123.45', '$434.23', '$567.89']
# >>> # o/p [123.45, 434.23, 567.89]

print([float(item[1:]) for item in items])

print()
# 144 Generator function for Fibonacci series program
print("Q.144")


def fibonanci(time):
    a = 0
    b = 1
    for _ in range(0, time):
        yield a
        c = a + b
        a = b
        b = c


res = fibonanci(10)
for ele in res:
    print(ele)

print()
# 145 Write a program to print common character present in all the items of the below list
print("Q.145")
items = ["glory", "glass", "sight", "fight"]
common = set(items[0])
for item in items:
    common = common.intersection(item)

print(common)

print()
# 146 Function should accept a list and if any number divisible by 3 then modify to 33 or else keep it as it is
print("Q.146")


def modify(list_):
    l = []
    for ele in list_:
        if ele % 3 == 0:
            l += [33]
        else:
            l += [ele]
    return l


print(modify([1, 4, 3, 5, 9, 21]))

print()
# 147  write a program to print the below pattern
print("Q.147")
#            1 2 3 *
#            1 2 * 4
#            1 * 3 4
#            * 2 3 4

key = 4
for _ in range(1, 5):
    for num in range(1, 5):
        if num != key:
            print(num, end='\t')
        else:
            print('*', end='\t')
            key -= 1
    print()


print()
# 148 write a program to map digits to its corresponding word
print("Q.148")
d = {   "0": "ZERO", "1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR",
        "5": "FIVE", "6": "SIX", "7": "SEVEN", "8": "EIGHT", "9": "NINE"
    }


def map_digit(key):
    return d.get(key, "unknown")


print(map_digit("3"))
print(map_digit('21'))

print()
# 149 validate if the list contains odd number at the beginning (0th index) and
# even numbers there after from 1st till end of the list
print("Q.149")
numbers = [1, 2, 4, 8, 6, 12] #----> the function should return True
numbers1 = [1, 2, 4, 7, 6, 12] #----> the function should return False
numbers2 = [2, 2, 4, 8, 6, 12] #----> the function should return False


def check(list_):
    if list_[0] % 2 == 1:
        for ele in range(1, len(list_)):
            if list_[ele] % 2 != 0:
                return False
        return True
    return False


print(check(numbers))
print(check(numbers1))
print(check(numbers2))

print()
# 150 sort the list of names based on lastname or first character of the lastname
print("Q.150")
names = ['steve jobs', 'bill gates', 'john doe', 'tim cook', 'laura turner', 'alex martin']
res = sorted(names, key=lambda item: item.split()[-1])
print(res)

res = sorted(names, key=lambda item: item.split()[0])
print(res)

print()
# 151 get all the pairs whose sum is 8
print("Q.151")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pair = []
for item in a:
    for ele in a:
        if item + ele == 8:
            pair.append([item, ele])

print(pair)

print()
# 152 write unique characters to the file
print("Q.152")
word = "aaabbbccc"

print("".join(sorted(set(word))))

print()
# 153 extract characters at even indexes of the string
print("Q.153")
items = (1, 2, 3, "bangalore", "mumbai")

print([item[::2] for item in items if isinstance(item, str)])

print()
# 154  Comparing two versions of the software
print("Q.154")
a = "1.3.4"
b = "2.4.5"
v1 = a.split(".")
v2 = b.split(".")
for i in range(len(v1)):
    if int(v1[0]) < int(v2[0]):
        print(f"{a} is lower version than {b}")
        break
    elif int(v1[1]) < int(v2[1]):
        print(f"{a} is lower version than {b}")
        break
    elif int(v1[2]) < int(v2[2]):
        print(f"{a} is lower version than {b}")
        break
    else:
        print(f"{a} is same version as {b}")


print()
# 155 Comparing two employee objects
print("Q.155")


class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay


e1 = Employee("steve", "jobs", 1000)
e2 = Employee("bill", "gates", 5000)
e3 = Employee("john", "cena", 3000)

d = [e1, e2, e3]

res = sorted(d, key=lambda item: item.fname)
for ele in res:
    print(ele.__dict__)
print('-' * 50)

res = sorted(d, key=lambda item: item.lname)
for ele in res:
    print(ele.__dict__)
print('-' * 50)

res = sorted(d, key=lambda item: item.pay)
for ele in res:
    print(ele.__dict__)

print()
# 156 Replace characters at odd index by 'x'
print("Q.156")
word = "example"

print("". join(["x" if index % 2 else value for index, value in enumerate(word)]))

print()
# 157  If the number is divisible by 2 it should print 'hi' if the no is divisible by 3
# it should print 'hello' if the number is divisible by both 2 and 3 it should print 'bye'.
# using list comprehension
print("Q.157")

some_list = [1, 4, 85, 32, 5, 6, 9]


def tackle(ele):
    if ele % 2 == 0 and ele % 3 == 0:
        return "bye"
    elif ele % 2 == 0:
        return "hi"
    elif ele % 3 == 0:
        return "hello"
    else:
        return ele


greet = [tackle(ele) for ele in some_list]
print(greet)

print()
# 158 even numbers using map and filter
print("Q.158")
nums = [10, 27, 30, 40, 53]

even = lambda num: num % 2 == 0

print(list(map(even, nums)))         # [T, F, T, T, F]
print(list(filter(even, nums)))     # [10, 30, 40]

print()
