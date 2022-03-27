"""
The functools module is  for the higher order functions
"""
from functools import cache
from math import factorial


@cache
def factorial_calc(n:int)->int:
    return factorial(n)

    