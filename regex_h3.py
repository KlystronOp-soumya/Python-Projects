import os
import re
# Enter your code here
def function(a):
    
    pattern=r"^[A-Z]{1}.*"
    result=re.match(pattern,a)
    
    return result
if __name__ == "__main__":
    a = input()
    b = function(a)


    if b:
        print(True)
    
    else:
        print(False)     