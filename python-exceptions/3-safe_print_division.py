#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except:
        return (None)
    finally:
        if result == None:
            print("Inside result: None")
        else:
            print("Inside result: {:.1f}".format(result))
    return (result)