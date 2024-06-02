
def swapElems(inputList , a , b):
    temp = inputList[a]
    inputList[a] = inputList[b]
    inputList[b] = temp
    print("here " ,inputList)


def sortListBubble(inputList) :
    #bubble sort
    n = len(inputList)

    #outer loop
    for i in range (0 , n-1 ) :
        for j in range ( 0 , n - i -1) :
            print("pass:" , i , "compare:" , j)
            if inputList[j] > inputList[j+1] :
                #swap
                #inputList[j] , inputList[j+1] = inputList[j+1] , inputList[j]
                swapElems(inputList , j , j+1)
                print("pass:{} current comparison:{}\n{}".format(i , i+1 , inputList))

    return

def sortListInsertion(inputList):
    pass

inputList=[3,-1,0,8,13,6]
print("list before sort:" , inputList)
sortListBubble(inputList)
print("list after sort:" , inputList)