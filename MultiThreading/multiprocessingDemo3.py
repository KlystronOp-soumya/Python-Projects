import os,math
from multiprocessing import Pool
def calc():
    for i in range(0,400000):
        math.sqrt(i)

processes=[] #List of threads

for i in range (os.cpu_count()):
    print("Registering the thereads %d"%i)
    processes.append(Pool(initializer=calc))
    
for process in processes:
    process.start()

for process in processes:
    process.join()
    