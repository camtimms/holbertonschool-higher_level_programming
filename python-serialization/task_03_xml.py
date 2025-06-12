#!/usr/bin/python3
"""
Serializing and Deserializing with XML

In this exercise we’ll explore serialization and deserialization using XML as an
alternative format to JSON.
"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    # Create root element
    root = ET.Element("data")

    # Use dict to fill key and value as child elements
    for key, value in dictionary.items():
        child_element = ET.SubElement(root, key)
        child_element.text = str(value)

    # Write and save xml element tree to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    # Parse and read file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Fill dictionary with child data
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return (dictionary)
