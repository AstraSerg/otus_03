from typing import TypeVar
"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
The type can only be str or int.
"""

T = TypeVar("T", int, str)

def add(a: T, b: T) -> T:
    return a + b

