# Simple program to demonstrate the binary file handling in Python
import os , sys , pickle
#get the class from the file
from EmployeeEntity import EmployeeEnity

def isFileExists(fileName:str , dirName:str) -> None:
    #check if the directory exists or not
    if(not os.path.isdir(dirName)) :
        #then create the directory
        os.mkdir(dirName)
    #check if the file is existed
    if (not os.path.isfile):
        #then create the file
        f = open(PATH+fileName , "w+")
        print(fileName , " was created : " , os.path.abspath(fileName)) 
    return

def createBinaryFile(fileName : str) -> None :
    
    return

def readBinaryFile(fileName : str) -> None :
    
    return

if __name__ == "__main__" :
     #call the functions
     PATH = "Documents\\"
     fileName = input("Enter the file name: ")
     #dirName = input("Enter the directory:")
     #call the functions
     # first check whether the file and dir is present or not
     isFileExists(fileName= fileName , dirName= PATH)
     