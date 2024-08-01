#!/usr/bin/env python3
"""
element_length - accept Iterable return list of tuples
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    lst: Iterable
    return list of tuple
    """
    return [(i, len(i)) for i in lst]
