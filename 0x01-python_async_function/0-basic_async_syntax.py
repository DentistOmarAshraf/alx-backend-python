#!/usr/bin/env python3
"""
Asyncio
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    max_delay - (int) random to choose from 0 to max_delay
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
