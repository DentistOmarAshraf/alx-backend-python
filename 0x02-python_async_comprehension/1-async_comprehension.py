#!/usr/bin/env python3
"""
Asyncio Comperhension
"""

from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Loop over asyncio generator and reuturn list of fload (results)
    """
    result: list[float] = [res async for res in async_generator()]
    return result
