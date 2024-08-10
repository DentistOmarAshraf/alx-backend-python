#!/usr/bin/env python3
"""
AsyncIO comperhension
"""

import asyncio
import time
from typing import List, Generator


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    meassure time of four async comperhension
    """
    start: float = time.time()
    tasks: List[Generator] = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end: float = time.time()
    elapsed_time: float = end - start
    return elapsed_time
