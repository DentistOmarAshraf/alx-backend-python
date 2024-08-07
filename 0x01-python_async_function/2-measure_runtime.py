#!/usr/bin/env python3
"""
AsyncIO
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function to measure time of asyncIO
    n: (int) number of times wait_random() function
    max_delay: (int)
    """
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.perf_counter() - start
    return end
