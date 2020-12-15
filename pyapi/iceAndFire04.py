#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)   #pprint is pretty print.
        # print(type(got_dj))
        houses = got_dj.get("allegiances")
        books = got_dj.get("books")
        print(f"You chose character: {got_charToLookup}, who is {got_dj.get('name')}, who is of the house(s) {houses} and can be read about int the books {books}")
        char_houses = []
        char_books = []
        print("\nThey are in the house(s):")
        for house in houses:
            house_info = requests.get(house)
            print(house_info.json().get("name"))
        print("\nthey can be found in the books:")
        for book in books:
            book_info = requests.get(book)
            print(book_info.json().get("name"))


if __name__ == "__main__":
        main()
