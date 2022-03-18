import asyncio
async def alice():
 print("Anything you can do I can do better.")
 print("I can do anything better than you.")
 await bob()
 print("Yes, I can.")
 await bob()
 print("Yes, I can.")
 await bob()
 print("Yes, I can. I can!")

async def bob():
 print("No you can't.")

asyncio.run(alice())