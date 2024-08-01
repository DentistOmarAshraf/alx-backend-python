#!/usr/bin/env python3
"""
sum_list - take a list of flaots
return sum of them (float)
"""


def sum_list(input_list: list[float]) -> float:
    """
    input_list - list of float
    return float
    """
    to_ret: float = 0.0
    
    for elem in input_list:
        to_ret += elem
    
    return to_ret
