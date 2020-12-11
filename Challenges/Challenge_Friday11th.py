#!/usr/bin/env python3

def howdy(name):
    print("Hello, " + name)


def multiply(num):
    print(f"11.0 times {num} = {num * 11}")


def adder(num1, num2):
    total = 0
    for num in range(num1, num2 + 1):
        total = total + num
    print("Your total is: ", total)


user = input("What is your name: ")
howdy(user)

nums = float(input("Please enter a number: "))
multiply(nums)

first = int(input("Enter a number between 1 and 10: "))
second = int(input("Enter a different number between 1 and 10: "))
if first > second:
    adder(second, first)
elif first < second:
    adder(first, second)
else:
    print("You entered the same number twice, that won't work.")
