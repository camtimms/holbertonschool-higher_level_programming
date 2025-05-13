#!/usr/bin/python3
def print_reversed_list_integer(mylist=[]):
    mylist.reverse()
    for i in range(len(mylist)):
        print("{}".format(mylist[i]))
