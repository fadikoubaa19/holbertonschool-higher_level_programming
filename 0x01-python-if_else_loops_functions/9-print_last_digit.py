#!/usr/bin/python3
def print_last_digit(a):
    if a < 0:
        num = (-a) % 10
    elif a == 0:
        num = a
    else:
        num = a % 10
    print("{:d}".format(num), end='')
    return(num)
