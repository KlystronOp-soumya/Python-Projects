import asyncio

async def myCoroutine():
    print("this is a simple Coroutine")

async def compile_myCoroutine():
    await myCoroutine()

loop = asyncio.get_event_loop()
loop.run_until_complete(compile_myCoroutine())
loop.close()