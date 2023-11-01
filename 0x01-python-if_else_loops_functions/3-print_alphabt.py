#!/usr/bin/python3
for str in range(ord('a'), ord('z') + 1):
    if (chr(str) not in 'qe'):
        print("{:c}".format(str), end="")
