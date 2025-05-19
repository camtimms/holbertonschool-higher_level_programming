#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return (None)
    if a_dictionary == {}:
        return(None)
    # max_value = max(a_dictionary.values())
    
    name = ""
    score = 0
    for key, value in a_dictionary.items():
        if value > score:
            score = value
            name = key
    return(name)
