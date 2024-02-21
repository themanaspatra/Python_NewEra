# Write a program to check if the given string is Palindrome or not
# with and without using reversed method.
s1 = "madam"
s2 = ""
for ele in s1:
    s2 = ele + s2
if s1 == s2:
    print(f"{s1} is pallindrome")
else:
    print(f"{s1} is not pallindrome")

# Replace "how" to "who" in the string "hi how are you" with and without inbuilt methods
s = "hi how are you"

string = s.replace("how", "who")
print(string)

l = []
for ele in s.split():
    if ele == "how":
        l.append("who")
    else:
        l.append(ele)
print(" ".join(l))

s1 = ""
for ele in s.split():
    if ele == "how":
        s1 = s1 + "who" + " "
    else:
        s1 = s1 + ele + " "
print(s1)

# Replace all the vowels with "*" in the string "hello world"

s = "hello world"
s_ = ""
for ele in s:
    if ele in "aeiouAEIOU":
        s_ += "*"
    else:
        s_ += ele
print(s_)

# Replace all the characters which occurs more than once with "*" in the string "hello world"

s = "hello world"
_s = ""
for ele in s:
    if s.count(ele) > 1:
        _s += "*"
    else:
        _s += ele
print(_s)

# Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
#  Output : java
filename = "abc.java"
extension = filename.split(".")[-1]
print(extension)

# convert a string to a list and vice-versa.
string = "welcome all"
converted_list = string.split()
print(converted_list)

converted_string = " ".join(converted_list)
print(converted_string)

# Covert the string "Hello welcome to Python" to a comma separated string.
string = "welcome to python world"
list_string = string.split()
print(",".join(list_string))

# Write a Program to print ascii values of the characters present in a string.
string = "welcome to python world"
for ele in string:
    print(f"ASCII value of {ele} --> {ord(ele)}")

# Find the longest word in the sentence
sentence = "Hello world. Welcome to Python"
temp = ""
for ele in sentence.split():
    if len(ele) > len(temp):
        temp = ele
print(f"the longest word is {temp}")

# Sum all the numbers in the below string.
s = "Sony12India567Pvt2ltd"
total = 0
for ele in s:
    if ele.isdigit():
        total += int(ele)
print(f"total is {total}")

# Program to print the number of occurrences of characters in a String without using inbuilt functions.
s = 'helloworld'
occur = {ele: s.count(ele) for ele in s}
print(occur)

# Program to print only the repeated characters and count of the same.
s = 'helloworld'
occur = {ele: s.count(ele) for ele in s if s.count(ele) > 1}
print(occur)

# Write a program to get alternate characters of a string
s = 'helloworld'
for ele in s[::2]:
    print(ele, end='\t')

print()
# Find the longest non-repeated substring in the below string
s = "This is a Programming language and Programming is fun"
temp = ""
for ele in s.split():
    if len(ele) > len(temp) and s.count(ele) == 1:
        temp = ele
print(f"longest non repeated word is --> {temp}")

longest_word = {ele: len(ele) for ele in s.split() if s.count(ele) == 1}
*other, len_pair = sorted(longest_word.items(), key=lambda item: item[-1])
print(len_pair)

# Write a program to count the number of white spaces in a given string
s = "this is python language"
count = 0
for ele in s:
    if ele == " ":
        count += 1
print(f"No. of whitespaces is ==> {count}")

# Write a program to rotate characters in a string
s = "awesome"
print(s[::-1])
s_ = ""
for ele in s:
    s_ = ele + s_
print(s_)

# Write a program to print only non-repeated characters in a string
s = "this is repeated"
repeat = {ele: len(ele) for ele in s if s.count(ele) == 1}
print(repeat)

# Write a program to print all the consonants in a given string
s = "awesome"
for ele in s:
    if ele not in "aeiouAEIOU":
        print(ele)

# Write a program to count no of capital letters in a string
s = "This is Python World"
count_upper = 0
for ele in s:
    if ele.isupper():
        count_upper += 1
print(f"no of capital letter --> {count_upper}")

# Write a program to find the first repeating character in a string
s = "hello world"
for ele in s:
    if s.count(ele) > 1:
        print(ele)
        break

# Write a program to find the index of nth occurrence of a sub-string in a string
sentence = "hello world welcome to python hello hi how are you hello there"

import re
matches = re.finditer(r'hello', sentence)
print(matches)
positions = [(match.start(), match.end()) for match in matches]
print(positions[0])

# Write a program to count the number of occurrences of non-special characters in a given string
s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
count = 0
for ele in s:
    if ele.isalnum():
        count += 1
print(f"fno of occurance of non special character is --> {count}")

# Filter only those characters except digits
s = '@hello12world34welcome!123'
s_ = ""
for ele in s:
    if not ele.isdigit():
        s_ += ele
print(s_)

# Find all max length words from the below sentence
sentence = "hello world hi apple you yahoo to you"
temp = sentence.split()[0]
l = []
for ele in sentence.split():
    if len(ele) >= len(temp):
        temp = ele
        l.append(temp)
print(l)

longest = max(sentence.split(), key=len)
l = []
for ele in sentence.split():
    if len(ele) == len(longest):
        l.append(ele)
print(l)
