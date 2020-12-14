#!/usr/bin/env python3

"""
This script reads email addresses and variations specified by the the user. Since many email addresses can end
with multiple variations, only the search string entered by the user will be used all the way to the end of that
address. .
"""

import re

def list_reader(search):
    # opens file to be read from
    search_file = open("email_list.txt", "r")
    # reads through the file
    search_file = search_file.readlines()
    # iterates through file
    for names in search_file:
        # checks for a match of the possible user names and corresponding email addresses.
        if re.search(rf"^{search}", names):
            print(names)


def main():
    user_name = input("Please enter the beginning of the user ids you'd like to search for: ")
    list_reader(user_name)

main()



