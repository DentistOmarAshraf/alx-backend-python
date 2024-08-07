#!/usr/bin/env python3
"""
Asyncio
"""

import asyncio
from typing import List, Awaitable

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    n - (int) loop limit
    max_delay: (int)
    """
    coroutines: list[Awaitable] = [wait_random(max_delay) for _ in range(n)]
    to_ret: list[float] = []
    for future in asyncio.as_completed(coroutines):
        to_ret.append(await future)
    return to_ret
