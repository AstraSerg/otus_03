from typing import TypeVar

"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
"""
T = TypeVar('T', int, str, list[str])


def add(a: T, b: T) -> T:
    return a + b

