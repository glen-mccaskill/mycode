#!/user/bin/env python3

import netifaces
# print(netifaces.interfaces())
# print(netifaces.ifaddresses("ens33"))

def ip_addr(interface):
    print('\n**************IP Address of Interface - ' + interface + ' *********************')
    print(netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr'])


def mac_addr(interface):
    print('\n**************MAC Address of Interface - ' + interface + ' *********************')
    print(netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr'])


for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
       print('MAC: ', end='')  # This print statement will always print MAC without an end of line
       print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'])  # Prints the MAC address
       print('IP: ', end='')  # This print statement will always print IP without an end of line
       print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'])  # Prints the IP address
    except:
        print("Could not collect adapter information")


print()
print(netifaces.interfaces())
adapter = input("Enter an adapter from the list:")

try:    # try/except done two separate times since it exits at first error.
    ip_addr(adapter)
except:
    print("Could not collect adapter information")
try:
    mac_addr(adapter)
except:
    print("Could not collect adapter information")