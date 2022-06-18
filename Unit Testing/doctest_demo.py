
from doctest import testmod
def fact(n):
    """The function returns the factorail of a number.
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(5)
    120

    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    """
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if(n == 0 or n ==1):
        return 1
    return n*fact(n-1)

if __name__ == "__main__":
    testmod()