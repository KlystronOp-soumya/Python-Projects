inputList= list()
inp= int(input("Enter the number of elements: "))
for i in range(inp):
    a= int(input("Enter the elements: "))
    inputList.append(a)
#if the user puts only a single element
if len(inputList) == 1 :
    print(inputList)
    exit(0)

print("Given list: ",inputList)
inputList.sort()
print(inputList)
for j in inputList:
    currentIndex = inputList.index(j)
    nextIndex = currentIndex+1
    if nextIndex < len(inputList) and inputList[currentIndex] == inputList[nextIndex] :
        print("t1")
        inputList.remove(j)
    
        
print("List without dupliate characters: ", inputList)