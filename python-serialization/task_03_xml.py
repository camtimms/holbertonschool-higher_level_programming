#!/usr/bin/python3
"""
Serializing and Deserializing with XML

In this exercise we’ll explore serialization and deserialization using XML as an
alternative format to JSON.
"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)

def deserialize_from_xml(filename):
    pass
