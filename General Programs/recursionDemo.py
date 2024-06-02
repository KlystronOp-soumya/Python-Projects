def loopDemo():
    for i in range(0, 11) :
        print(i , end=" ")
    print()
def recursionDemo(start: int) -> None :
    if(start == 11):
        return
    print(start,end=" ")
    recursionDemo(start+1)

def power(base: int  , indices: int) -> int:
    
    #brak condition
    if(indices == 0):
        return 1
    else:
        return base * power(base, indices -1 )

loopDemo()
recursionDemo(0)
print(power(2,3))
    