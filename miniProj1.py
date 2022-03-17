#!/bin/python3

import math
import os
import random
import re
import sys



class IncreasingList:

    def __init__(self):
        super().__init__()
        self.lst = list() #initializes an empty list
        
    def append(self, val):
        """
        first, it removes all elements from the list that have greater values than val, starting from the last one, and once there are no greater element in the list, it appends val to the end of the list
        """
        pass

    def pop(self):
        """
        removes the last element from the list if the list is not empty, otherwise, if the list is empty, it does nothing
        """
        pass

    def __len__(self):
        """
        returns the number of elements in the list
        """
        return 0
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    lst = IncreasingList()
    q = int(input())
    for _ in range(q):
        op = input().split()
        op_name = op[0]
        if op_name == "append":
            val = int(op[1])
            lst.append(val)
        elif op_name == "pop":
            lst.pop()
        elif op_name == "size":
            fptr.write("%d\n" % len(lst))
        else:
            raise ValueError("invalid operation")
    fptr.close()