#!/usr/bin/env python3

if "n" not in ["nope", "no-way", "no-how"]:
    print("Yes this was True")
else:
    print("That was a false statement")

# this is actually evaluating if the string "n" is in this list. It is not parsing strings.

if "n" not in ["nope", "no-way", "no-how", "n"]:
    print("Yes this was True")
else:
    print("That was a false statement")

if "n" in "nope, no-way, no-how":
    print("n is there")
else:
    print("No it isn't there.")