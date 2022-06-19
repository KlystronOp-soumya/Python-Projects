import os
import re

# Enter your code here
def function(a):
    
    pattern=r"^[AEIOU].*$"
    match = re.match(pattern,a,re.IGNORECASE)
    
    return match

if __name__ == "__main__":
    a = input()
    b = function(a)


    if b:
        print(True)
    
    else:
        print(False)     