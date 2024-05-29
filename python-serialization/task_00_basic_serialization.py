#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize the Python dictionary 'data' to a JSON file specified by 'filename'.
    
    Parameters:
    data (dict): The dictionary to serialize.
    filename (str): The name of the file to save the serialized data.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load and deserialize the JSON data from the specified file to a Python dictionary.
    
    Parameters:
    filename (str): The name of the file to load the JSON data from.
    
    Returns:
    dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
