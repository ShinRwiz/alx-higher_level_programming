#!/usr/bin/python3
"""
appends a string
"""


def append_write(filename="", text=""):
    """number of characters added:"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
