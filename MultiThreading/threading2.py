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
t1=threading.Thread(target=calc_square,args=(ar,))
t2=threading.Thread(target=calc_cube,args=(ar,))

t1.start()
t2.start()

t1.join()
t2.join()
print("Time passed: ",time.time()-t)
