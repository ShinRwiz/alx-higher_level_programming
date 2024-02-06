#!/usr/bin/python3
"""
خbject to a text file
"""

import json


def save_to_json_file(my_obj, filename):
    """خbject to text file using a JSON"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
