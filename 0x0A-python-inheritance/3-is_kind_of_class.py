#!/usr/bin/python3
"""
is_kind_of_class Function
"""


def is_kind_of_class(obj, a_class):
    """True = obj is an instance or inherited from a_class else = False"""
    return (isinstance(obj, a_class))
