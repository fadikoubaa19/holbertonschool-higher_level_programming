#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number % 10) > 5:
    print("{:d} is {:d} and greater than 5".format(number, number % 10))
elif (number % 10) == 0:
    print("{:d} is {:d} and is 0".format(number, number % 10))
else:
    print("{:d} is {:d} and is is less than 6 and not 0" /
           .format(number, number % 10))
