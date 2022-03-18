"""
Use this for multiple arguments
print(p.starmap(f, [(1,2), (3,4), (5,6)])
"""
import time
import os
from multiprocessing import Pool

def f(x):
 return x*x

p = Pool(5)
print(p.map(f, [1, 2, 3]))

p.close()
p.join()