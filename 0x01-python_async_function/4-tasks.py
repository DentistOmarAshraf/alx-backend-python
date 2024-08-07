#!/usr/bin/env python3
"""
AsyncIO
"""

import asyncio
from typing import List, Awaitable

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    n - (int) loop limit
    max_delay: (int)
    """
    coroutines: list[Awaitable] = [task_wait_random(max_delay)
                                   for _ in range(n)]
    to_ret: list[float] = []
    for future in asyncio.as_completed(coroutines):
        to_ret.append(await future)
    return to_ret
