import numbers
import time
from multiprocessing import Pool

def sum_sq(number):
    sum=0
    for i in range(number):
        sum+=i*i
    
    return sum

def sum_sql_with_mp(numbers):
    start_time=time.time()
    p=Pool()
    result=p.map(sum_sq,numbers)
    p.close()
    p.join()

    end_time=start_time-time.time()

    print(f"Processing{len(numbers)} numbers took {end_time} time to proecess.")
def sum_sq_no_mp(numbers):
    start_time=time.time()
    result=[]
    for i in numbers:
        result.append(sum_sq(i))

    end_time=start_time-time.time()

    print(f"Processing{len(numbers)} numbers took {end_time} time to proecess with out multiprocessing.")

if __name__ == "__main__":
    numbers=range(100)
    sum_sql_with_mp(numbers)
    sum_sq_no_mp(numbers)