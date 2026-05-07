#!/usr/bin/python3
"""Defines a BaseGeometry class with integer validator."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raise an Exception - area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a value as a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
