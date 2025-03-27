# my_library/__init__.py
"""
My Library - A description of what this library does.

This module provides functionality for...
"""

from .version import __version__
from .core import main_function, process_data
from .utils import utility_function

__all__ = [
    '__version__',
    'main_function',
    'process_data',
    'utility_function',
]

