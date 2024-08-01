#!/usr/bin/env python3
"""
zoom_array - duplicate entry tuple
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    lst: tuple
    factor: int , default = 2
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in
