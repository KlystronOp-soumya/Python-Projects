import os , sys
def createFile():
    with open("Documents\\myFile.txt" , "w+" , 1024)  as myFile :
        print("Enter @ to stop inserting lines")
        str=None #initializing
    while(str != '@') :
        str=map(int ,input() )
        #write the string into file
        myFile.write(str+"\r\n")

    return

def readFile(fileName : str) -> None:
    #now show the contents of the file we created:
    #path = "Documents\\" + fileName
    print("\nShowing the contents of the file\n")
    with open(PATH + fileName, "r" , 1024)  as myFile :
        #fileContents = myFile.read()
        fileContents = myFile.readline()
        print(fileContents)
        #print(fileContents.split('.'))
        # we can also read all the lines at once
    return
        
# Python program to show the file append features

def writeFileAndShow(fileName:str) -> None :
    inputContent = None
    with open(PATH+fileName , "a+" , 1024) as myFile :
       while(inputContent != '@'):
           inputContent = input()
           if(inputContent != "@") :
               myFile.write(inputContent)
    
    # Get the position of the cursor
    print(myFile.tell())
    #reset the cursor / file pointer
    myFile.seek(0 , 0)
    
    print("The file contents are: ")
    fileContents = myFile.read()
    print(fileContents)
    return

def getFileContents(fileName:str) -> list :
    
    return

if __name__ == "__main__" :
    PATH = "Documents\\"
    #createFile()
    readFile(fileName="lorem.txt")