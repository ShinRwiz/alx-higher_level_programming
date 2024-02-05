#!/usr/bin/python3
"""
Function inherits_from
"""


def inherits_from(obj, a_class):
    """True = obj is a subclass of a_class else = false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
