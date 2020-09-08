#!/usr/bin/python3
for c in range(97, 123):
    if not (c == 113 or c == 101):
        print("{:c}".format(c), end='')
