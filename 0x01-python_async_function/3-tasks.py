#!/usr/bin/env python3
"""
AsyncIO
"""
import asyncio
from typing import Awaitable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    max_delay: int
    return asyncio Task
    """
    task: asyncio.Task = asyncio.create_task(wait_random(max_delay))
    return task
