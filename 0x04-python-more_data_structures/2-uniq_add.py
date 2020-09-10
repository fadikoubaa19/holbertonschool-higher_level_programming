#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_one = []
    a = 0
    for i in my_list:
        if i not in new_one:
            new_one.append(i)
            a += i
    return a
