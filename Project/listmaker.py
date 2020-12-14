#!/usr/bin/env python3

import random
import csv

user_names = ["pgriffith", "stewieg", "bsimpson", "marges", "homer"]

email_domains = ["hotmail.com", "gmail.com", "yahoo.com", "outlook.com", "mail.com"]


listfile = open("email_list.txt", "a")

for names in user_names:
    for mails in email_domains:
        val = random.randint(1, 4)
        if val >= 2:
            val2 = random.randint(1, 20)
            email_address = names + str(val2) + "@" + mails
        else:
            email_address = names + "@" + mails
        print(email_address)
        print(email_address, file = listfile)

listfile.close()

