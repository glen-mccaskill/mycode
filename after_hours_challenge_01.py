#!/usr/bin/env python3

cars = ["Mustang", "GTO", "Corvette", "Yugo"]
print("{0}, {1}, and {2} are a fast type of car. {3}, not so much.".format(*cars))

cars.insert(3, "Pinto")
print("{0}, {1}, and {2} are a fast type of car. {3}, not so much.".format(*cars))

cars.append("Gremlin")
print("{0}, {1}, and {2} are a fast type of car. {4} and {5}, not so much.".format(*cars))

cars.pop()
print(cars)

movies = {"action": "Terminator", "comedy": "Friday"}
print(f"I like watching {movies['action']}, but sometimes {movies['comedy']} is good, too.")
print(movies.keys)
print(movies.values)
print(movies.get("romantic"))

crazy_string = "ThIs iS a StRaNge string with numbers like 4 18 42 and special characters +! - *"
print(crazy_string.upper().split("I"))
print(crazy_string.title())
print(crazy_string.lower())

