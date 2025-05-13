#!/usr/bin/python3
def new_tuple(tuple_a):
    if len(tuple_a) == 1:
         new_tuple = (tuple_a[0], 0)
    elif len(tuple_a) == 0:
         new_tuple = (0, 0)
    else:
         new_tuple = tuple_a
    return (new_tuple)

def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = new_tuple(tuple_a)
    tuple_b = new_tuple(tuple_b)

    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    add_tuple = (a, b)
    return (add_tuple)
