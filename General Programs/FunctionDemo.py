"""
This script demonstrates different functions which uses loops and other
features of python
"""

#this is a function

"""
def is the keyword which declares a function
syntax: def fun_name (arguments)
"""

def showAll (li=None,st=None , tpl = None , dct= None): #None is like Null in Java
    #iterating through the list
    for i in range(len(li)):
        print("{}# {}\n".format(i,li[i]))
    
    #iterating through dictionary
    for key,value in dct.items() :
        print("{} : {} \n".format(key,value))

if __name__ == "__main__" :
    li=["Debjani",1,2.3,[1,2,3,4]] #this is a list
    st = (1,2,3,4,3,4,5) #this is a set
    tpl= {1,2,3,4,5}
    dct={"name1" : "Debjani","name2" : "Naba" , "name3" : "Soumik" }

    showAll(li,st,tpl,dct)
