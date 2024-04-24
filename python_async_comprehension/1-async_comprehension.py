#!/usr/bin/env python3

import asyncio
import random

async def async_comprehension():
    return [random.random() * 10 for _ in range(10)]

async def main():
    print(await async_comprehension())

if __name__ == "__main__":
    asyncio.run(main())
