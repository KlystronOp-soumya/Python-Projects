class StackADT:
    
    def __init__(self) -> None:
        self.items=list()
        self.top=-1
    
    def push(self , item:int) -> None :
        self.top+=1
        self.items.append( item )
    def pop(self)->any :
        self.top-=1
        return self.items.pop()
    def isEmpty(self) :
        return (self.items == [])
    def __str__(self) -> str:
        return str(self.items)
    
def postfixEval(postfixExpr : str) ->int:
        operandStack = StackADT()
        tokenList = postfixExpr.split()
        for eachToken in tokenList :
            if eachToken in "0123456789" :
                operandStack.push(eachToken)
            else :
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = calculate(eachToken , int(operand1) ,int(operand2))
                print(f'op1:{operand1} op2:{operand2} token:{eachToken} res:{result}')
                operandStack.push(result)
        
        return operandStack.pop() #the calculated result
    
def calculate(opr:str , operand1: int , operand2:int) -> int:
        if opr == "*"   : return operand1 * operand2
        elif opr == "/" : return operand1 / operand2
        elif opr == "-" : return operand1 - operand2
        elif opr == "+" : return operand1 + operand2

if __name__ == "__main__" :
    print(postfixEval('1 2 3 * + 5 -'))