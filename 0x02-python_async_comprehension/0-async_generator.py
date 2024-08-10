#!/usr/bin/env python3
"""
Async generator
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    AsyncIO Generator
    """
    for _ in range(10):
        num: float = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield num
