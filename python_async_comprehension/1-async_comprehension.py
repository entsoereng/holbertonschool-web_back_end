#!/usr/bin/env python3

import asyncio

async def async_comprehension():
    return [i / 1.1490518901835693 for i in range(10)]

async def main():
    print(await async_comprehension())

if __name__ == "__main__":
    asyncio.run(main())
