import threading
def fn(n):
    print(n*n)

t1 = threading.Thread(target=fn, args=(5,))
t2 = threading.Thread(target=fn, args=(6,))

t1.start()
t2.start()