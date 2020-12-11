#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0   # counter for fails
logingood = 0
# open the file for reading
with open("/home/glen/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            print(line)
            print(line.split(" ")[-1])
            loginfail += 1  # this is the same as loginfail = loginfail + 1
        elif " -] Authorization failed" in line:
            logingood += 1  # successful login possibility.

print("The number of failed log in attempts is", loginfail)
print("The number of successful log in attempts is", logingood)
