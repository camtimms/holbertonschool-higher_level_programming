#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    flag = True
    i = 0
    while flag:
        try:
            print(f"{my_list[i]}", end="")
            i += 1
        except:
            flag = False
            print()
    
    return (i)            
