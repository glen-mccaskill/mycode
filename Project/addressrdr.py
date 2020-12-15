#!/usr/bin/env python3

"""
This script reads email addresses and variations specified by the the user. Since many email addresses can end
with multiple variations, only the search string entered by the user will be used all the way to the end of that
address. Additionally, the file to be searched will be selected by the user.
"""

import re
import argparse


def list_reader(search, where):
    howmany = 0
    # opens file to be read from in read only mode
    search_file = open(where, "r")
    # reads through the file
    search_file = search_file.readlines()
    # iterates through file
    for names in search_file:
        # checks for a match of the possible user names and corresponding email addresses.
        if re.search(rf"^{search}", names):
            # this is a counter for matches.
            howmany += 1
            print(names, end="")

    print()
    print(f"This search returned {howmany} matches from {where}.")


def main():
    # sets up argument parsing
    parser = argparse.ArgumentParser()
    # userid to be searched for.
    parser.add_argument("user", type=str, help="the userid to search for")
    # file to be searched through.
    parser.add_argument("--file", type=str, help="the filename to search", default="list.txt")
    args = parser.parse_args()
    # assign variable to pass to function that will actually do the searching.
    user_name = args.user
    file1 = args.file
    # invoke the function with userid and filename.
    list_reader(user_name, file1)

main()




