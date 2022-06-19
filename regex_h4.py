import os
import re

# Enter your code here. Read input from STDIN. Print output to STDOUT
def main(x):
    pattern=r"\b([A-Z][a-z]+|[A-Za-z]?)\s+\w+\s+(\d+)\b"
    matches= re.finditer(pattern, x)
    names=[]
    values=[]
    dicts=[]
    for matchNum, match in enumerate(matches, start=1):

        names.append(match.group(1))

        values.append(match.group(2))

    dicts= dict(zip(names, values))

    

    return dicts
    
    return dicts
    '''For testing the code, no input is to be provided'''

if __name__ == "__main__":
    x=input()
    print(main(x))