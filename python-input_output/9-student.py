#!/usr/bin/python3
"""
Name: Student
Description: Class that holds information about a student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Converts to dict"""
        return (self.__dict__)
