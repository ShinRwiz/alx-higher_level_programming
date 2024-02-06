#!/usr/bin/python3
"""
json str function
"""

import json


def from_json_string(my_str):
    """object represented by a JSON string"""
    return json.loads(my_str)
