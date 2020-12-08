#!/usr/bin/env python3

dog_names = ["Tiny", "Sissy", "Spot"]
cat_names = ["Fluffy", "Mittens", "Tabby"]

dog_names.append(cat_names)
print(dog_names[0])
print(dog_names[3][1])

critters = {"first_dog": dog_names[0], "second_cat": dog_names[3][1]}
print(critters)
print(critters.values())

