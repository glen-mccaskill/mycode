#!/usr/bin/env python3

proto = ["ssh", "http", "https"]
print(proto)
print(proto[1])
proto.extend("dns")     # adds d, n, and s, not dns. brackets needed for dns. No brackets, iterates through.
proto.extend(["dns"])
proto.append("dns")     # adds dns because append adds one item at the end.
print(proto)

proto2 = [22, 80, 443, 53]  # list of common ports: ssh, http, https, dns
proto.extend(proto2)        # passing second list to extend first list
print(proto)
proto.append(proto2)        # treats list being passed as one item. Demonstrated by following loop.
print(proto)
print()

for num in range(len(proto)):
    print(proto[num], end="----")
    print(num)
