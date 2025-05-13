#!/usr/bin/python3
def max_integer(mylist=[]):
    if mylist == []:
        return (None)
    
    max_int = 0
    for i in mylist:
        if i > max_int:
            max_int = i
    return (max_int)