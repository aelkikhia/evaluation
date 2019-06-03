#!/usr/bin/python3
"""Bench mark utility for testing speed of functions"""

import time
from functools import wraps


def time_this(func):
    """
    decorator function timer
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper
