#!/usr/bin/python3
def safe_print_division(a, b):
    i = 0
    j = 0
    try:
        i = a / b
        return i
    except ZeroDivisionError:
        i = None
        return(None)
    finally:
        print("Inside result: {}".format(i))
        return(j)
