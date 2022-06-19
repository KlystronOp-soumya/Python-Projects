import os

from collections import *


# Enter your code here.

#namedtuple

def func1(x,y):

    sal = namedtuple('player','name,runs')

    s= sal(x,y)

    return s

#deque

def func2(s):

    mal = [s]

    d=deque(mal)

    return d

#Counter

def func3(x):

    e=Counter(x)

    return e

#Ordereddict    

def func4(m,n,o,p,q):

    d=OrderedDict()

    d[1]=m

    d[2]=n

    d[3]=o

    d[4]=p

    d[5]=q

    return d

#defaultdict    

def func5(a,b):

    s=defaultdict(list)

    s[0]=a;

    s[1]=b;

    return s
    '''For testing the code, no input is to be provided'''

if __name__ == "__main__":
    a,b=input().split()
    x=func1(a,b)
    print(x)
    
    line = input().split()
    x=func2(line)
    print(x)
    
    a=list(map(int, input().split()))
    x=func3(a)
    print(x)
    
    a,b,c,d,e=input().split()
    x=func4(a,b,c,d,e)
    print(x)
    
    a,b=input().split()
    x=func5(a,b)
    print(x)