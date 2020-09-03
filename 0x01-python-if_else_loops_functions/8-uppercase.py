#!/usr/bin/python3
def uppercase(str):
    l = len(str)
    for i in range(0, l):
        if ord(str[i]) in range(97, 123):
            a = chr(ord(str[i]) - 32)
        else:
            a = str[i]
        print("{:s}".format(a), end='')
    print()
