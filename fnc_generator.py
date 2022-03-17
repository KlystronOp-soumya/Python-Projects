
"""Function that calculates the magic number :
  f(n) = n(n^2+1)/2
"""
def magic_number(n):
    return (n*(pow(n,2)+1))//2

def generator_Magic(n1):
    # Write your code here
    """Generator to generate from 3 to n1 """
    for i in range(3,n1+1):
        yield magic_number(i)

if __name__ == '__main__':

    n = int(input().strip())
    
    for i in generator_Magic(n):
        print(int(i))

    gen1 = generator_Magic(n)
    print(type(gen1))
#or with out using the for loop
    gen = generator_Magic(n)
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())

