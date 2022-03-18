import asyncio
import time

async def co_fn(msg):
    await asyncio.sleep(1)
    print(msg)

async def main():
    task1 = asyncio.create_task(
        co_fn('hello'))

    task2 = asyncio.create_task(
        co_fn('world'))

    await task1
    await task2

asyncio.run(main())