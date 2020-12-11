#!/usr/bin/env python3

def howdy(name):
    print("Hello, " + name)


def multiply(num):
    print(f"11.0 times {num} = {num * 11}")


def adder(list):
    total = 0
    for num in list:
        total = total + list[num]
    print("Your total is: ", total)

user = input("What is your name: ")
howdy(user)

nums = float(input("Please enter a number: "))
multiply(nums)

first = int(input("Enter a number between 1 and 10: "))
second = int(input("Enter a different number between 1 and 10: "))
if first > second:
    numlist = range[second, first,1]
elif first < second:
    numlist = range[first, second,1]
else:
    print("You entered the same number twice, that won't work.")

adder(numlist)