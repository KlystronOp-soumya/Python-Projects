#Script to implement stack in Python using array
import random , sys

class StackADT :
    def __init__(self , capacity=1) -> None:
        self.top = -1 #to mark the top element
        self.capacity = capacity  #capacity of the array
        self.arr = [None] * capacity #initialized with None
    
    def push(self , data:int ) -> None :
        """_summary_
           method to push elements into the stack
           checks for Stack overflow 
        Args:
            data (int): _description_
                        data to be inserted into the stack
        Returns:
            data: None
        """
        if self.capacity == self.top+1 :
            print("Stack Overflow")
            return
        
        self.top +=1
        self.arr[self.top] = data

    def pop(self) -> int :
        """_summary_
           returns the top element and removes it from the top
           Checks for empty stack 
        Returns:
            int: _description_
                popped element
        """
        if self.top == -1 :
            print("Stack underflow")
            return
        temp = self.arr[self.top]
        self.top-=1
        #make efficient resize
        if self.top < self.capacity//2:
            print("Trying to resize: Decrease")
            self.capacity = self.capacity//2
            newArr = [None]*self.capacity
            for i in range(0 , self.top+1):
                newArr[i] = self.arr[i] #copy the elements
            
            self.arr = newArr #refer to the new one
        
        return temp

    def peek(self)->int :
        """_summary_
           Returns the top most element in the stack
           Checks for the empty stack
        Returns:
            int: _description_
                topmost element in the array
        """
        if self.top == -1 :
            print("Stack Underflow")
            return
        
        return self.arr[self.top]
    
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top+1 == self.capacity

if __name__ == "__main__" :
    stack = StackADT(10)
    for x in range(10) :
        stack.push(random.randint(1,21))
    print(stack.arr)
    for x in range(12) :
        temp = stack.pop()
        if temp is not None :
            print(temp)

        
        
        
        