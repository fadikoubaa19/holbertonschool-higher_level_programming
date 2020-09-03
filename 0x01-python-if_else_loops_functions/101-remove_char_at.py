#!/usr/bin/python3
def remove_char_at(str, n):
    word = ""
    l = len(str)
    for c in range(0, l):
        if c != n:
            newstr = word + str[c]
    return(newstr)
