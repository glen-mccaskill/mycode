#!/usr/bin/env python3

critters = ["Fox", "Fly", "Ant", "Bee", "Cod", "Cat", "Dog"]
numlist = [1, 2, 3, 4]
print(numlist)

easiest = "{} {} {} {} {} {} {}".format(*critters)
print(easiest)

print(" ".join(critters))

for num in range(len(critters)):
    print(critters[num], end=" ")
print()

print(critters)
critters.remove("Ant")
print(critters)
critters.reverse()
print(critters)
critters.insert(3, "Yak")
print(critters)
critters.sort()
print(critters)

rooms = ["living", "dining", "bath"]
bedrooms = ["master", "kid1", "kid2", "guest"]
rooms.insert(1, bedrooms)   # inserting a list inside another list.
print(rooms)
print(rooms[1][3])  # displays index 1's 3rd index.
