#!/usr/bin/env python3

fi = input("Please enter the file you would like to load: ")
## create file object in "r"ead mode
with open(fi, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)
print("Lines in your file:",len(configlist))

## display list with no "\n"
print(configlist)
