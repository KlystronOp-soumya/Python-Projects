
def getPoppedBookCount(bookIdList=None , requestedBookIDList=None):
    """_summary_

    Args:
        bookIdList (List, mandatory): _description_. Defaults to None.
        requestedBookIDList (List, mandatoru): _description_. Defaults to None.
    
    Returns:
           popCountList: _description_. count of the books required to pop to get the target book id
    """
    popCountList= list()
    POP_COUNT = 0
    tempList=[]
    if bookIdList != None and requestedBookIDList != None:
        for eachBookId in requestedBookIDList :
           print("Scanned id: " , eachBookId)
           if eachBookId not in bookIdList:
               popCountList.append(-1)
           else:
               bookIdList.reverse()
               print("before: " , bookIdList)
               for ids in bookIdList[::-1]:#iterating backwards
                   if ids != eachBookId:
                        print("Inside if current book list id scanned: " , ids)
                        tempList.append(bookIdList.pop())
                        POP_COUNT+=1
                        print("Current temp:" , tempList ," pop count:" , POP_COUNT)
                   else:
                       print("inside else current book list id scanned: " , ids)
                       bookIdList.pop() #remove the matched element
                       popCountList.append(POP_COUNT+1) #increase the count to include the popped element
                       print("Current popCountList:" , popCountList)
                       POP_COUNT=0 #reset the value
                       while tempList: #insert into same order
                          bookIdList.append(tempList.pop())
                       tempList.clear()
                       print("bookList:" , bookIdList)
                       break
    return popCountList
    


if __name__ == "__main__" :
    book_stack = list() #list with book ids
    user_request = list() #user given ids
    
    #take the book id inputs
    while(1):
        bookId = int(input())
        if bookId != -1 :
            book_stack.append(bookId)
        else:
            break
    
    #take the user input
    while(1):
        requestedBookId = int(input())
        if requestedBookId != -1:
            user_request.append(requestedBookId)
        else:
            break
    print(book_stack)
    print(user_request)
    print(getPoppedBookCount(book_stack , user_request))

