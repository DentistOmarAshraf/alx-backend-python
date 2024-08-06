#!/usr/bin/env python3
"""
Asyncio
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    n - (int) loop limit
    max_delay: (int)
    """
    delays: List[float] = []
    all_delays: List[float] = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        result = await delay
        all_delays.append(result)

    return all_delays.sort()
