# Write program to merge two different lists.
l1 = [1, 2, 4, 5]
l2 = [3, 7, 8]

l3 = l1 + l2
print(l3)
print([*l1, *l2])

# Remove duplicates from the list without using inbuilt functions
l1 = [1, 4, 2, 4, 1, 8]
unique_l = list(set(l1))

print(unique_l)

# How to get the elements that are in list b but not in list a
a = [1, 2, 3]
b = [1, 2, 3, 4]

for ele in b:
    if ele not in a:
        print(ele)

# Print all the numbers in the below list
a = ['abc', '123', 'hello', '23']

print([int(ele) for ele in a if ele.isdigit()])

# Write a program to get alternate characters of a string in list format.
string = "awesome"

print([ele for ele in string[::2]])

# Write a program to iterate through list and build a new list,
# only if the items of the list has even number of characters.
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']

new_list = [name for name in names if len(name) % 2 == 0]
print(new_list)

# Write a program to reverse the list as below

words = ["hi", "hello", "python"]
# o/p ['nohtyp', 'olleh', 'ih']
out = [word[::-1] for word in words[::-1]]
print(out)

# Write a list comprehension to get a list of even numbers from 1-50
print([no for no in range(1, 50) if no % 2 == 0])


# "Write a program to find the duplicate elements in the list without using inbuilt functions
names = ['apple', 'google', 'apple', 'yahoo', 'google']

print(list(set(names)))

# "Write a program to count the number occurrences of each item in the list without using any inbuilt functions
names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']

print({name: names.count(name) for name in names})

# "Write a program to find the largest number in the list without using any inbuilt functions

numbers = [10, 20, 30, 40, 50]
temp = numbers[0]
for no in numbers:
    if no > temp:
        temp = no

print(f"largest no is {temp}")

# Write a program to find most common words in a given list.

words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into','my', 'eyes', "you're", 'under']

word_count = {word: words.count(word) for word in words}
most, *other = sorted(word_count.items(), key=lambda item: item[-1], reverse=True)
print(most)


from collections import Counter

count_word = Counter(words)
print(count_word.most_common()[0])

# Write a program to get all the duplicate items and the number of times the item is repeated in the list.
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']

print({name: names.count(name) for name in names if names.count(name) > 1})

# Write a program to print all numeric values in a list
items = ['apple', 1.2, 'google', '12.6', 26, '100']

print([item for item in items if isinstance(item, (int, float))])

# Write a program to rotate items of the list
items = ['apple', 1.2, 'google', '12.6', 26, '100']

print([item[::-1] if isinstance(item, str) else item for item in items])

# Write a program to rotate characters in a string
items = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']

print([item[::-1] for item in items])

# Write a program to check if the elements in the second list is series of continuation of the items
# in the first list

a = [10, 12, 14, 16, 18]
b = [20, 22, 24, 26, 28]
differ = b[0] - a[0]
for ele in range(len(b)):
    if b[ele] - a[ele] != differ:
        print("discontinue")
        break
else:
    print("it is a continuation of series")

# "Write a program to sort a list which has mix of both odd and even numbers,
# the sorted list should have odd numbers first and then even numbers in sorted order
a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
odd = []
even = []
for ele in a:
    if ele % 2 == 0:
        even.append(ele)
    else:
        odd.append(ele)
odd.sort()
even.sort()
print([*odd, *even])

# Write a program to sort a list which has mix of both odd and even numbers, in the sorted list,
# odd numbers should be in ascending order and even numbers should be in descending order
a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
odd = []
even = []
for ele in a:
    if ele % 2 == 0:
        even.append(ele)
    else:
        odd.append(ele)
odd.sort()
even.sort(reverse=True)
print([*odd, *even])

# Find all max numbers from the below list
numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
maxx = max(numbers)
all_max = []
for no in numbers:
    if no == maxx:
        all_max.append(no)
print(all_max)

# "Write a program to sum all even numbers in the given string
sentence = 'hello 123 world 567 welcome to 9724 python'

print(sum([int(ele) for ele in sentence if ele.isdigit() and int(ele) % 2 == 0]))

# Comprehensions
# -----------------
# Square Numbers in the list. Using List list_Comprehensions
l = [1, 2, 4, 5]

print([ele ** 2 for ele in l])

# List of even numbers between range 1-50

print([ele for ele in range(1 ,51) if ele % 2 ==0])

# Returns a list names starting with vowels in the given string
names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']

print([name for name in names if name[0] in "aeiouAEIOU"])

# Filtering all the languages which starts with 'p'
languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']

print([lan for lan in languages if lan[0].lower() == 'p'])

# Names starting with consonants
names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']

print([name for name in names if name[0] not in "aeiouAEIOU"])

# Filtering out those names which are less than 6 characters
names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']

print([name for name in names if len(name) < 6])

# Raise to the power of list index
a = [1, 2, 3, 4, 5]

print([ele ** index for index, ele in enumerate(a)])

# Build a list of tuples with string and its length pair
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

print([(name, len(name)) for name in names])

# Build a list with only with even length string
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

print([name for name in names if len(name) % 2 == 0])

# Generating List of PI values
# o/p: [3.0, 3.1, 3.14, 3.141]

# List comprehension to sum the factorial of numbers from 1-5
from math import factorial

print(sum([factorial(no) for no in range(1, 6)]))

# Reverse the item of a list if the item is of odd length string
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

print([name[::-1] if len(name) % 2 == 1 else name for name in names])
