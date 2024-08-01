#!/usr/bin/env python3
"""
safely_get_value - accept dictionary and return a dict[key] else default
"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    dct: dictionary (Mapping)
    key: (any)
    dafault: variale type T or None
    return T type or any
    """
    if key in dct:
        return dct[key]
    else:
        return default
