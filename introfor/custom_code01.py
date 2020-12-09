#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for x in farms:
    print("Information is : " + str(x))

# Displays the information, but instructions were vague. Not sure if supposed to be formatted.
# Not sure if more efficient way to do this. Pulled dictionaries from list, then internal list from
# resulting dictionaries. Iterated through internal list with nested loop.

print(len(farms))

for stuff in range(len(farms)):         # getting the length of the list
    temp_dict = farms[stuff]            # pulling dictionary from list index
    print("Farm Name:")
    print(temp_dict.get("name"))    # pulling "name"'s value from dictionary.
    print()
    print("Products:")
    temp_list = (temp_dict.get("agriculture"))  # pulling list from values of key.
    for items in temp_list:                         # iterating through resulting list created by previous line.
        print(items, end=" ", flush=True)
    print()
    print()
