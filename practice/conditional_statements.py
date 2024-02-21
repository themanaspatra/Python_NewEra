# check if the iterable is empty
some_iterable = (1,)
if not isinstance(some_iterable, (int, float, complex, bool)):
    if some_iterable:
        print(f"{some_iterable} is not empty")
    else:
        print(f"{some_iterable} is empty")

# greatest of 3 numbers
a = 5
b = 15
c = 10
if a > b and a > c:
    print(f"{a} is greater than {b}, {c}")
elif b > a and b > c:
    print(f"{b} is greater than {a}, {c}")
else:
    print(f"{c} is greater than {a}, {b}")

# converting upper to lower and vice versa
string = "iT"
new_string = ""
for ele in string:
    if ele.isupper():
        new_string += ele.lower()
    elif ele.islower():
        new_string += ele.upper()
print(new_string)

# check if entered character is vowel or not
string = "m"
for ele in string:
    if ele in "aeiouAEIOU":
        print(f"{string} is vowel")
    else:
        print(f"{string} is consonant")

# check if entered character is vowel or not, if it is vowel then create a dictionary with char and its ascii value pair
string = "a"
some_dict = {}
for ele in string:
    if ele in "aeiouAEIOU":
        some_dict[ele] = ord(ele)
        print(some_dict)
    else:
        print(f"{string} is consonant")

# check if the key is present , if present then increment or initialize the value to 1
d = {'a': 1, 'b': 2, 'c': 3}
key = "m"

# if key in d:
#     d[key] += 1
# else:
#     d[key] = 1
# print(d)

print(d.get(key, 0) + 1)

# check if the given value is string or not
value = "string"
if isinstance(value, str):
    print("It is a string")

# check if the given number is even or odd
value = 15
if value % 2:
    print(f"{value} is odd")
else:
    print(f"{value} is even")

# check whether the string is palindrome or not
string = "madam"
if string[::-1] == string:
    print(f"{string} is a pallindome")
else:
    print(f"{string} is not pallindrome")

# check if the integer is palindrome or not
value = 102
if int(str(value)[::-1]) == value:
    print(f"{value} is pallindrome")
else:
    print(f"{value} is not pallindrome")

# check if the given year is leap year or not
year = 2024
if year % 4 == 0:
    print(f"{year} is a leap year")
elif year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# check if the given character is number or alphabet or special character
character = "a"
if character.isalpha():
    print("it is an alphabet")
elif character.isdigit():
    print("it is number")
else:
    print("it is a special character")

# check if the given number is perfect square or not
num = 100
if str(num)[-1] not in "2378":
    print("it is perfect square")
else:
    print("it is not a perfect square")

# check if the entered marks is greater than 35 then print pass, else print fail,
# if the marks is above 60 print first class
mark = "37"
if int(mark) > 35:
    print("you are pass")
elif int(mark) > 60:
    print("you got first class")
elif int(mark) < 35:
    print("you are failed")

# check if the given string is starting with vowel or not
string = "important"
if string[0] in "aeiouAEIOU":
    print("the given string start with vowel")
else:
    print("the given string does not start with vowel")

# check if the given string is ending with vowel or not
string = "important"
if string[-1] in "aeiouAEIOU":
    print("the given string ends with vowel")
else:
    print("the given string does not end with vowel")

# check if the list has even numbers of elements
l = [1, 5, 3, 4, 7, 8, 9]
if len(l) % 2 == 0:
    print(f"{l} have even number of element")
else:
    print(f"{l} have odd number of element")

# check the number of keys in the dictionary, if the number is even print the dictionary as it is,
# else add a new key to make it even and print it
d = {'a': 10, "b": 20, "c": 30}
if len(d) % 2 == 0:
    print(d)
else:
    d['new_key'] = "value"
    print(d)

# In a number check if the first number is even or odd
num = 225
if int(str(num)[0]) % 2 == 0:
    print(f"{num} first number is even")
else:
    print(f"{num} first number is odd")

# In a number check if the second last number is even or odd
num = 1254451
if int(str(num)[-2]) % 2 == 0:
    print(f"{num} second last is even")
else:
    print(f"{num} second last is odd")
