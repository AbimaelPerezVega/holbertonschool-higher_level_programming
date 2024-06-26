#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON and write it to 'data.json'.
    
    Parameters:
    csv_filename (str): The name of the CSV file to read from.
    
    Returns:
    bool: True if conversion is successful, False if an error occurs.
    """
    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} does not exist.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
