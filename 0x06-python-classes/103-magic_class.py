#!/usr/bin/python3
"""m"""
import math


class MagicClass:
    """c"""
    def __init__(self, radius=0):
        """m"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """c"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """c"""
        return 2 * math.pi * self.__radius
