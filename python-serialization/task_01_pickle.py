#!/usr/bin/python3
"""
Pickle

Description: A task designed to learn about binary serialization using pickle
"""
import pickle


class CustomObject:
    """
    Basic Object to track student information

    Contains the following atributes:
    name, age, is_student
    """

    def __init__(self, name, age, is_student) -> None:
        """Constuctor"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
        filename: The filename of the output serialized binary data
        """
        try:
            with open(filename, "wb") as f:
                data = pickle.dump(self, f)
                return (data)
        except TypeError:
            raise TypeError("Cannot serialize object")

    @classmethod
    def deserialize(cls, filename):
        """
        cls: Class to be created from data
        filename: File name to load the data from
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return (obj)
        except TypeError:
            raise TypeError("Cannot deserialize object")
        except EOFError:
            raise pickle.UnpicklingError("Corrupted pickle file")

    def display(self):

        """
        Display the data of the object
        """
        print(
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Is Student: {self.is_student}\n"
        )
