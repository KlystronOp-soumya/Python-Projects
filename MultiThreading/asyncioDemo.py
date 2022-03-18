import asyncio
import random
"""
Lightweight threads
"""
async def myCoroutine(id):
    process_time=random.randint(1,5)
    await asyncio.sleep(process_time)
    print("COroutine with ID: {} took time:{} ".format(id,process_time))

""" @asyncio.coroutine
def myCoroutine2():
    print("My corutine") """

async def main():
    tasks=[]

    for i in range(10):
        tasks.append(asyncio.ensure_future(myCoroutine(i)))


    await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
