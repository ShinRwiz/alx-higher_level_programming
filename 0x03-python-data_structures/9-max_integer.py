#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    temp = my_list.copy()
    temp.sort()
    return temp[-1]
