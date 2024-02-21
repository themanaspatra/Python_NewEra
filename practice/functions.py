# A function takes variable number of positional arguments as input. How to
# check if the arguments that are passed are more than 5

def func(*args):
    if len(args) > 5:
        return f"more than 5 arguments passed"


print(func(1, 4, 5, 7, 8,6))

# Write a function to print the below output.
# func(""TRACXN"", 0)  # Should print RCN
# func(""TRACXN"", 1)  # Should print TAX"

def func1(some_value):
    if some_value == "TRACXN":
        return 0
    elif some_value == "TRAXCN":
        return 1


print(func1("TRACXN"))
print(func1("TRAXCN"))

# Write a function to check if the number is Prime


def check_prime(some_num):
    for num in range(2, some_num):
        if some_num % num == 0:
            print(f"{some_num} is not prime")
            break
    else:
        print(f"{some_num} is prime")


check_prime(3)
check_prime(4)

# Write a method that returns the last digit of an integer. For example, the call of
# get_last_digit(3572) should return 2.

def get_last_digit(some_num):
    return some_num % 10


print(get_last_digit(3525))

# Make a function named tail that takes a sequence (like a list, string, or tuple)
# and a number n and returns the last n elements from the given sequence, as a list.


def tail(sequence, num):
    return sequence[-num:]


print(tail([1, 5, 7, 2, 4], 2))
print(tail("awesome", 4))

# Write function named is_perfect_square that accepts a number and returns True if it's a perfect square
# and False if it's not.
from math import sqrt


def is_perfect_square(num):
    if round(sqrt(num)) ** 2 == num:
        return True
    else:
        return False


print(is_perfect_square(90))

# Write a function which returns the sum of lengths of all the iterables


def len_sum(iterable):
    total_len = len(iterable)
    return sum(range(total_len+1))


print(len_sum([4, 1, 2, 5]))

# Python function to check whether a number is Prime or not


def check_prime(some_num):
    for num in range(2, some_num):
        if some_num % num == 0:
            print(f"{some_num} is not prime")
            break
    else:
        print(f"{some_num} is prime")


check_prime(5)

# Python function  to check if a given number is Fibonacci number?


def check_fibonacci(some_num):
    l = []
    a = 0
    b = 1
    for _ in range(some_num ** some_num):
        l.append(a)
        c = a + b
        a = b
        b = c
    if some_num in l:
        return f"{some_num} is fibonanncci number"
    return f"{some_num} is not a fibonancci number"


print(check_fibonacci(2))

# Write a function to build a list of prime numbers from 1-50.


def prime(some_num):
    prime_list = []
    for num in range(1, some_num+1):
        for no in range(2, num):
            if num % 2 == 0:
                break
        else:
            prime_list.append(num)
    return prime_list


print(prime(50))

# Write a function to return a list by reversing the item of a list
# if the item is of odd length string otherwise keeping the item as is!.
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']


def some_func(some_list):
    return [ele if len(ele) % 2 == 0 else ele[::-1] for ele in some_list]


print(some_func(names))
