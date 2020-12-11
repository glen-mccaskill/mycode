#!/usr/bin/env python3
import subprocess  ## <-------- changed
subprocess.call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")
# interface = input("Enter an interface, like, ens3: ")
# subprocess.call(["ip", "addr", "show", "dev", interface])  ## <--- changed
# subprocess.call(["ip", "route", "show", "dev", interface]) ## <--- changed
print("-"*50)
subprocess.call(["ping", "-c 4", "8.8.8.8"])
subprocess.call(["traceroute", "8.8.8.8"])
subprocess.call(["du","-h", "/home/glen/mycode"])