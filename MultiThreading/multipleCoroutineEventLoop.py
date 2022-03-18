"""
This program demonstrates the multiple coroutine execution 
and the event loop

In order to execute the async we need a event loop
"""

import asyncio

async def myCoriutineOne():
    
    while True:
        await asyncio.sleep(0.1)
        print("Coroutine 1")
async def myCoroutineTwo():
    while True:
        await asyncio.sleep(0.1)
        print("Coroutine 2")

if __name__ =="__main__" :
    try:
        loop=asyncio.get_event_loop()
        asyncio.ensure_future(myCoriutineOne())
        asyncio.ensure_future(myCoroutineTwo())
        loop.run_forever()
    except KeyboardInterrupt as kbi:
        print(kbi)
    finally:
        print("Closing the event loop..")
        loop.close()
