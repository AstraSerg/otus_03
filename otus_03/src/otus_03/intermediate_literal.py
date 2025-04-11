from typing import Literal

"""
TODO:

foo only accepts literal 'left' and 'right' as its argument.
"""
Direction = Literal["left", "right"]

def foo(direction: Direction) -> str:
    return direction

