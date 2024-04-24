#!/usr/bin/env python3
''' Async Comprehension '''

from typing import List
Vector = List[float]

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Vector:
    ''' Function that returns a list '''
    return [number async for number in async_generator()][:10]

# Test the function
async def test_async_comprehension():
    result = await async_comprehension()
    print(result)

# Run the test
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_async_comprehension())
