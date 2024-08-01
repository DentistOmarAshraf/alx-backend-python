#!/usr/bin/env python3
"""
to_kv - take a key of string and value of int or float
return tuple (str, float)
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    k: string (key)
    v: float or int
    return tuple(k, v)
    """
    return tuple([k, v**2])
