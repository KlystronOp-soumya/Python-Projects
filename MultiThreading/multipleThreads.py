"""
Example of the global interpreter lock or GIL
"""
from asyncio import threads
import os,math
from threading import Thread

def calc():
    for i in range(0,400000):
        math.sqrt(i)

    threads=[] #List of threads

    for i in range (os.cpu_count()):
        print("Registering the thereads %d"%i)
        threads.append(Thread(target=calc))
    
    for thread in threads:
        thread.start()

for thread in threads:
    thread.join()
    