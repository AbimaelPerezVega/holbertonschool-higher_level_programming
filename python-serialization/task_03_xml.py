#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    
    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the file to save the XML data.
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.
    
    Parameters:
    filename (str): The name of the file to read the XML data from.
    
    Returns:
    dict: The deserialized Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    
    return dictionary
