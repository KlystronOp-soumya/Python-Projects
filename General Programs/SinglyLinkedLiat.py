class Node:
    """ This class implemenets the Node of a Linked List
    """
    
    def __init__(self) -> None:
        self.data = None
        self.next = None
       
    
    def setData(self,data) :
        self.data = data

  
    def getData(self):
        return self.data
    
    
    def setNext(self,next):
        self.next = next
    
   
    def getNext(self):
        return self.next

    def hasNext(self)->bool:
        return self.next != None  


    
    

class SinglyLinkedList:
    length = -1


    def __init__(self) -> None:
        self.head = Node()

    
    def countNodes(self)->int:
        """ This method counts the number of nodes present in the
         Linekd List
        """
        current = self.head #refers to the head node
        count = 0

        if self.head is None :
             raise Exception("LinkedList has not been created")
        
        while current.getNext() != None:
            current = current.getNext()
            count+=1
           
        return count

    
    
    def appendNode(self,data)->None :
        #define two node
        if self.head != None :
            temp= Node()
            temp.setData(data)
            temp.setNext(None)
            self.head = temp
        else:
            temp=self.head
            while temp.getNext() != None:
                temp= temp.getNext()
            
            r= Node()
            r.setData(data)
            r.setNext(Node)
            temp.setNext(r)
        
        self.length += 1
    

    def insertAtBegining (self,data)->None:
        temp_node = Node()
        temp_node.setData(data)
        temp_node.setNext(None)

        if self.length == 0:
            self.head = temp_node
        else:
            temp_node.setNext(self.head)
            self.head = temp_node
        self.length +=1

    def insertAtPos(self,pos,data):
        if pos > self.length or pos < 0:
            raise Exception("No Such position exists")
        else:

            if pos == 0 :
                self.insertAtBegining(data)
            else:
                if pos == self.length :
                    self.appendNode(data)
                else:
                    temp_node = Node()
                    temp_node.setData(data)
                    count = 0 
                    current = self.head

                    while count < pos+1:
                        count+=1
                        current = current.getNext()
                    
                    #similar to r->next_node_address = temp->next_node_address
                    temp_node.setNext(current.getNext())
                    #temp->next = r
                    current.setNext(temp_node)

                    self.length+=1

    def showLinkedList(self):
        temp = self.head
        while temp.getNext() is not  None :
            print(f'{temp.getData()}->',end='')
            temp=temp.getNext()


if __name__ == "__main__" : 
    try:
        head = SinglyLinkedList()
        head.insertAtBegining(13)
        print(head.countNodes())
        head.showLinkedList()
    except Exception as e :
        print(e)




