#!/usr/bin/env python3

round = 0
answer = " "

while round < 3 and answer.lower() != "brian" and answer.lower() != "shrubbery":
    round += 1  # format to add what's right of += to the variable left of +=
    answer = input("Finish the movie title, 'Monty Python\'s The Life of _____'")
    if answer.lower() == "brian":
        print("Correct!")
    elif answer.lower() == "shrubbery":
        print("You got the super secret answer!")
    elif round == 3:
        print("Sorry, the answer was Brian.")
    else:
        print("Sorry, try again!")
