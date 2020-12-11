#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""
from colorama import Fore, Back, Style

# function to push commands
def commandpush(devicecmd):     # devicecmd==list
    for coffeetime in devicecmd.keys():
        print(Fore.LIGHTYELLOW_EX + 'Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print(Fore.GREEN + 'Attempting to sending command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here
def devicereboot(iplist):
    for ip in iplist:
        print(Fore.GREEN + "Connecting to...." + ip)
        print(Fore.RED + "REBOOTING NOW!" + Fore.GREEN)

# start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}
    # data that replaces data stored in file

    stuff = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    print("Welcome to the network device command pusher")   # welcome message

    # get data set
    print("\nData set found\n")     # replace with function call that reads in data from file

    # run
    commandpush(work2do)    # call function to push commands to devices
    print()
    devicereboot(stuff)
# call our main function
main()