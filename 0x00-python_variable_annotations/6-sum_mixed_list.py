#!/usr/bin/env python3
"""
sum_mixed_list - take a list of int and float
and return float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    list - mixed array (float and int)
    return float (sum of them)
    """
    to_ret: float = 0.0

    for elem in mxd_lst:
        to_ret += elem

    return to_ret
