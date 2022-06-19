import os

import builtins

import pickle

import sys

sys.tracebacklimit=0

import traceback

import io

from logging import Logger


safe_builtins = {

 'range',

 'complex',

 'set',

 'frozenset'

}

class RestrictedUnpickler(pickle.Unpickler):


    def find_class(self, module, name):

        # Only allow safe classes from builtins.

        if module == "builtins" and name in safe_builtins:

            return getattr(builtins, name)

        raise pickle.UnpicklingError("global '%s.%s' is forbidden" % (module, name))

        # Forbid everything else.

        


def restricted_loads(s):

        return RestrictedUnpickler(io.BytesIO(s)).load()


def func1(a):

    try:

        x= restricted_loads(pickle.dumps(a))

        return x

    except pickle.UnpicklingError :

        s=traceback.format_exc()

        

        return s



def func2(s):

    try:

        x= restricted_loads(pickle.dumps(slice(0,8,3)))

        return s[x]

    except pickle.UnpicklingError :

        s=traceback.format_exc()

        return s


    

if __name__ == "__main__":

       a=range(int(input())) 

       b=func1(a)

       print(b)

       print("Traceback (most recent call last):")

       y=tuple(input())

       z=func2(y)

       print(z)