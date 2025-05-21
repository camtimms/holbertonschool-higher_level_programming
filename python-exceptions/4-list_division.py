#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    num = 0
    den = 0
    results = []
    i = 0
    while i < list_length:
        try:
            result = my_list_1[num] / my_list_2[den]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            results.append(result)
        num += 1
        den += 1
        i += 1
    return (results)
