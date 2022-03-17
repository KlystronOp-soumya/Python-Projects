class Comp:
    def __init__(self,real=None,imaginary=None) -> None:
        self.real = real
        self.imaginary = imaginary
    
    def add(self,obj2)->None:
        realSum= self.real + obj2.real
        imagSum = self.imaginary+obj2.imaginary
        
        print("Sum of the two Complex numbers :{}{}{}i".format(str(realSum),"+",str(imagSum))) 

    def sub(self,obj2)->None:
        realSub= self.real - obj2.real
        imagSub = self.imaginary-obj2.imaginary
        if imagSub >= 0:

            print("Subtraction of the two Complex numbers :{}{}{}i".format(str(realSub),"+",str(imagSub))) 
        else:
            print("Subtraction of the two Complex numbers :{}{}i".format(str(realSub),str(imagSub)))


if __name__ == '__main__':
    
    real1 = int(input().strip())
    img1 = int(input().strip())
    
    real2 = int(input().strip())
    img2 = int(input().strip())
    
    p1 = Comp(real1,img1)
    p2 = Comp(real2,img2)

    p1.add(p2)
    p1.sub(p2)