#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if sentence == "":
        return(l, None)
    a = sentence[0:1]
    b = (l, a)
    return(b)
