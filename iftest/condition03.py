#!/usr/bin/env python3

hostname = input("What value should we set for hostname?")

# to ensure that wrong case creates a false negative, convert string to lower case and compare.
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

print("Exiting the script")
