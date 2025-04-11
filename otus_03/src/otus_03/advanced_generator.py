"""
TODO:

`gen` is a generator that yields a integer, and can accept a string sent to it.
It does not return anything.
"""
from typing import Generator

def gen(x: str = "") -> Generator[int, str, None]:
    """You don't need to implement it"""
    yield 1

