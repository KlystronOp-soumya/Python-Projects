"""
Hackerrank multithreading Hands On one
"""
import threading

def square_it(n):
    print(f"square of {n}: {n*n}")

def do_it(a,b):
    t1=threading.Thread(target=square_it,args=(a,))
    t2=threading.Thread(target=square_it,args=(b,))

    t1.setName("Thread t1")
    t2.setName("Thread t2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__" :
    do_it(3,2)
    do_it(25,7)
