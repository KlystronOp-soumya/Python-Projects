
def isPrime(num = None):
    flag=True

    if ((num is not None) and ( num != 0 and num != 1)):
        for i in range (2 , (num//2)+1) :
            if num%i == 0 :
                flag = False
                break
    else:
        print("Not prime")
        flag = False
       

    return flag
       
if __name__ == "__main__":
    
    for i in range (1,101):
        if isPrime(i) :
            print( i , end=" , ")
        
        