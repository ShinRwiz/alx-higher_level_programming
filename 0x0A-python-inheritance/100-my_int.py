#!/usr/bin/python3
"""
MyInt Class
"""


class MyInt(int):
    """placeholder of comment"""
    def __new__(cls, *args, **kwargs):
        """New instance of class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """from != to =="""
        return int(self) != other

    def __ne__(self, other):
        """from == to !="""
        return int(self) == other
