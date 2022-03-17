def getPrimeList(maxRange):
    listOfPrimes=[]
    flag = False
    for i in range (2,maxRange+1):
        for j in range(2,(i//2)+1):
            if(i%j == 0):
                flag=True
                break
        if(not flag):
            listOfPrimes.append(i)
        else:
            flag = False
    
    #print(*listOfPrimes)
    return listOfPrimes


def primegenerator(num, val):
    # Write your code here
    if val == 1:
        for i in getPrimeList(num)[0::2]:
            yield i 
    if val == 0:
        for i in getPrimeList(num)[1::2]:
            yield i


if __name__ == '__main__':

    num = int(input().strip())

    val = int(input().strip())

    for i in primegenerator(num, val):
        print(i,end=" ")