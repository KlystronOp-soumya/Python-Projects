import time
import threading

def calc_square(ar):
    for nums in ar:
        time.sleep(0.2)
        print("Sqaure of ",nums,": ",nums*nums)

def calc_cube(ar):
    for nums in ar:
        time.sleep(0.2)
        print("Cube of ",nums,": ",nums*nums*nums)

ar=[2,3,4,5,6]
t=time.time()
calc_square(ar)
calc_cube(ar)

print("Time passed: ",time.time()-t)
