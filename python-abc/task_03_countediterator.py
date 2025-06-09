#!/usr/bin/python3

class CountedIterator():
    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self.__counter = 0

    def get_count(self):
        return (self.__counter)

    def __next__(self):
        try:
            value = self.iterator.__next__()
            self.__counter += 1
            return value
        except StopIteration:
            raise
