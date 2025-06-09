#!/usr/bin/python3

class CountedIterator():
    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self.__counter = 0

    def get_count(self):
        return (self.__counter)

    def __next__(self):
        self.__counter += 1
        return self.iterator.__next__()
