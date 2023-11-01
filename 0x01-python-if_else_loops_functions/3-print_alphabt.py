#!/usr/bin/python3
for str in range(ord('a'), ord('z') + 1):
    if str != ord('e') and str != ord('q'):
        print("{:c}".format(str), end="")
print()
