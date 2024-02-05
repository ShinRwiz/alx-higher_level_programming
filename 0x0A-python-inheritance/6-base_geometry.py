#!/usr/bin/python3
"""
BaseGeometry Class
"""


class BaseGeometry:
    """Public attribute area"""
    def area(self):
        """Exception when called"""
        raise Exception("area() is not implemented")
