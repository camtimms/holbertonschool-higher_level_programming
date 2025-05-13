#!/usr/bin/python3
def multiple_returns(sentance):
    length = len(sentance)

    if length == 0:
        first_char = None
    else:
        first_char = sentance[0]

    tuple = (length, first_char)
    return (tuple)
