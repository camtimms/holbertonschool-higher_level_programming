#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i, val in enumerate(my_list):
        if val == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])

    return (new_list)
