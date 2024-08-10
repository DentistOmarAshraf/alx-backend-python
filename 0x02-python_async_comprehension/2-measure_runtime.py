#!/usr/bin/env python3
"""
AsyncIO comperhension
"""

import asyncio
import time



async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    start: float = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    end: float = time.time()
    return end - start
