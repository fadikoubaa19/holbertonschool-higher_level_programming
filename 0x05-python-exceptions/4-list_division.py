#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    a = len(my_list_1)
    b = len(my_list_2)
    for i in range(list_length):
        try:
            t = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print('division by 0')
            t = 0
        except TypeError:
            print('wrong type')
            t = 0
        except IndexError:
            print('out of range')
            t = 0
        finally:
            new_list.append(t)
    return(new_list)
