#!/usr/bin/env python3
"""
AsyncIO
"""
import asyncio
from typing import Awaitable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable[float]:
    """
    max_delay: int
    return asyncio Task
    """
    return asyncio.create_task(wait_random(max_delay))