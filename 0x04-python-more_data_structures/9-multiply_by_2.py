#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    couple_dic = {}
    for i in a_dictionary:
        couple_dic[i] = a_dictionary[i] * 2
    return couple_dic
