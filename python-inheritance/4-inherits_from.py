#!/usr/bin/python3
"""Defines a function to check inherited class instance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherited
    from a_class, but not an instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
