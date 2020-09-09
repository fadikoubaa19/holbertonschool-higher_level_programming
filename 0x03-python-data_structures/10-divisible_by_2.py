#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    added = []
    for number in my_list:
        if number % 2 == 0:
            added.append(True)
        else:
            added.append(False)
    return added
