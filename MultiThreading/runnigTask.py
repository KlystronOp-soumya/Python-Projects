import asyncio
import time

async def co_fn(msg):
    await asyncio.sleep(1)
    print(msg)

async def main():
    await co_fn('Hello')
    await co_fn('world')

asyncio.run(main())
