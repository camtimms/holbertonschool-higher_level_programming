#!/usr/bin/python3
""" MyList is a custom class inherited from List """


class MyList(list):
    """ Inherited custom list class """
    def print_sorted(self):
        print(sorted(self))
