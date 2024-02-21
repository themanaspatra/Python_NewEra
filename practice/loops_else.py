# 1. write a program to check if the list has an even number or not.
print("Q.01")
l = [1, 4, 7, 5]
count = 0
for _ in l:
    count += 1
if count % 2 == 0:
    print(f"given list contain even no of element --> {l}")

print()
# 2. write a program for linear search
print("Q.02")


def linear(data, find):
    for index, item in enumerate(data):
        if item == find:
            print(f"{find} is in {index} index")


linear([1, 4, 8, 2], 4)

print()
# 3. write a program to check if the given numbers are the perfect squares within 100
print("Q.03")


def perfect(num):
    from math import sqrt
    no = round(sqrt(num))
    if no ** 2 == num and no < 100:
        print(f"{num} is a perfect square")
    else:
        print(f"{num} is not a perfect square")


perfect(90)

print()
# 4. write a program to check if the all the given words are palindromes
print("Q.04")


def pallindrome(str1):
    if str1 == str1[::-1]:
        print(f"{str1} is a pallindrome")
    else:
        print(f"{str1} is not a pallindrome")


pallindrome("madam")

print()
# 5. write a program to print if the given number is a prime number or not
print("Q.05")


def prime(num):
    for no in range(2, num):
        if num % no == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")

prime(5)
prime(10)

print()
