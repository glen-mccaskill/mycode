#!/usr/bin/env python3

round = 0
while True:
    round = round + 1
    print("Finish the movie title, 'Monty Python\'s The Life of _____'")
    answer = input("Your guess-->")
    if answer.lower() == 'brian':
        print("Correct!")
        break   # breaks out of while loop.
    elif round == 3:
        print("Sorry, the answer was Brian.")
        break   # breaks out of while loop.
    else:
        print("Sorry, try again!")
