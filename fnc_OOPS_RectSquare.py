#!/bin/python3

import math
import os
import random
import re
import sys



# Write your code here

class rectangle:
    def __init__(self):
        super().__init__()
    
    def area(self,l,b):
        print("Area of Rectangle is  {}".format(l*b))
    
    def display(self):
        print("This is a Rectangle")
        
class square:
    def __init__(self):
        super().__init__()
    
    def area(self,s):
        print("Area of square is  {}".format(s**2))
    
    def display(self):
        print("This is a Square")
        
if __name__ == '__main__':
    
    l = int(input())
    b = int(input())
    s = int(input())

    obj1 = rectangle()
    obj1.display() 
    obj1.area(l,b)

    obj2 = square()
    obj2.display()
    obj2.area(s)
