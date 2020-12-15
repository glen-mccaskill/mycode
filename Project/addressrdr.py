#!/usr/bin/env python3

"""
This script reads email addresses and variations specified by the the user. Since many email addresses can end
with multiple variations, only the search string entered by the user will be used all the way to the end of that
address. Additionally, the file to be searched will be selected by the user.
"""

import re
import argparse



def list_reader(search, where):
    # opens file to be read from
    search_file = open(where , "r")
    # reads through the file
    search_file = search_file.readlines()
    # iterates through file
    for names in search_file:
        # checks for a match of the possible user names and corresponding email addresses.
        if re.search(rf"^{search}", names):
            print(names)


def main():
    parser = argparse.ArgumentParser()
    # creates the user argument - userid to be searched for
    parser.add_argument("user", type=str, help="the userid to search for")
    # creates the file argument - file to be searched
    parser.add_argument("file", type=str, help="the filename to search")
    args = parser.parse_args()
    user_name = args.user
    file1 = args.file
    # pass user id and file to be searched.
    list_reader(user_name, file1)

main()




