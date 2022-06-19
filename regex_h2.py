import os
import re
def function(a):
    pattern=r"(e\w+|E\w+)\W(e\w+|E\w+)"
    m=re.match(pattern,a,re.IGNORECASE)
    
    return m
if __name__ == "__main__":
    a = input()
    b = function(a)


    if b:
        print(True)
    
    else:
        print(False)     