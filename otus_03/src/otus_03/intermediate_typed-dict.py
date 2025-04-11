from typing import TypedDict
"""
TODO:

Define a class `Student` that represents a dictionary with three keys:
- name, a string
- age, an integer
- school, a string
"""

class Student(TypedDict):
    """Typed dict."""
    name: str
    age: int
    school: str

