#!/usr/bin/env python3
"""
Asyncio
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    n - (int) loop limit
    max_delay: (int)
    """
    list_return = []
    for _ in range(n):
        list_return.append(await wait_random(max_delay))

    return list_return
