#!/usr/bin/env python3

"""
This script reads email addresses and variations specified by the the user. Since many email addresses can end
with multiple variations, only the search string entered by the user will be used all the way to the end of that
address. Additionally, the file to be searched can be selected by the user, or a default file will be used.
Author | Glen McCaskill
License | GPL-3.0 License
"""

import re
import argparse
import os.path
from os import path

def list_reader(search, where):
    howmany = 0
    domainlist = []
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
            # splitting the userid from the domain at the @ sign
            userid, domain = names.rsplit("@")
            # start building the list of domain occurrences.
            domainlist.append(domain)
            # printing the complete email addresses that were obtained from the file
            print(names, end="")

    print()
    print(f"This search returned {howmany} matches from the file: {where}")

    # sorting the list to put all identical domains together.
    domainlist.sort()
    # using a while loop to give a report on number of addresses from each domain.
    while len(domainlist) != 0:
        # obtaining the domain at index 0.
        dom_name = domainlist[0]
        # counting the number of identical domains.
        dom_count = domainlist.count(dom_name)
        # printing the number of occurrences of this domain with numbers aligned.
        print(f"{domainlist.count(dom_name):3} were from {dom_name}", end="")
        # removing the listed domains from the list
        del domainlist[0:dom_count]


def main():
    # sets up argument parsing
    parser = argparse.ArgumentParser()
    # userid to be searched for.
    parser.add_argument("user", type=str, help="the userid to search for")
    # file to be searched through.
    parser.add_argument("--file", type=str, help="the filename to search, or default file", default="list.txt")
    args = parser.parse_args()
    # assign variable to pass to function that will actually do the searching.
    user_name = args.user
    file1 = args.file
    
    if not path.exists(file1):
        print("That file does not exist. Try again with a valid filename.")
    else:
        # invoke the function with userid and/or optional filename.
        list_reader(user_name, file1)



if __name__ == "__main__":
    main()
