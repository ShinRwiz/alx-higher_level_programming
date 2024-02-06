#!/usr/bin/python3
"""
create an خbject from json
"""

import json


def load_from_json_file(filename):
    """create object from json """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
