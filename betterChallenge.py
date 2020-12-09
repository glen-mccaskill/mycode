#!/usr/bin/env python3

dog_names = ["Tiny", "Sissy", "Spot"]
cat_names = ["Fluffy", "Mittens", "Snowball"]

# Putting the two lists into a dictionary. Can also put dictionary inside a list.
pets = {"dogs": dog_names, "cats": cat_names}

print(pets["dogs"][0])
print(pets["cats"][1])

txt = "Why was he talking about a dumb kangaroo?!?"

snake_case = "Is the preferred naming convention in Python"

print(txt.upper())
print(txt)
print(txt.title())
print(txt.split())
print(txt.split("a"))

url = "https://alta3.com"
print(url)
print(url.lstrip("https://").rstrip(".com"))

cats = ["Fluffy", "Mittens", "Snowball"]
print("---".join(cats))     # prints out the elements of the list, individually with --- between them.

