#!/usr/bin/env python3
"""
make_multiplare - float argment return function (float)
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    multiplier : float
    return callable function
    """
    def func(arg: float):
        return multiplier * arg

    return func
