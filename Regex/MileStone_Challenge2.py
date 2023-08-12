#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'arrange' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#
import re
def arrange(sentence):
    # Write your code here
    patternCaps=r'[A-Z]'
    patternSmall = r'[a-z]'
    cPatternCaps = re.compile(patternCaps)
    cPatternSmall = re.compile(patternSmall)
    cFnlStrPattern = re.compile(r'^[A-Z][a-z]*\.$')
    fnlStr=str()
    #lastWord = getLastWordInSentence(sentence)
    lenDict=dict()
    for eachWord in sentence.split(' '):
        if(eachWord.find(".") > -1):
            indexAt = eachWord.index('.')
            eachWord = eachWord[:indexAt]
        key=len(eachWord)
        print(eachWord , ": " , key)
       
    
        if(lenDict.get(key) is not None): #if exists the add    
            wrdList = lenDict.get(len(eachWord))
            wrdList.append(eachWord) #add the current word
            lenDict[key] =  wrdList
        else:
            wrdList=[]
            wrdList.append(eachWord)
            lenDict[key] = wrdList
    
    eachKeys = sorted(lenDict.keys())
    #dubug
    for key  in eachKeys:
        print(key,"=>" , lenDict.get(key) , end=" ")
     
        tempList = lenDict.get(key)
        print("\nKey under scan: " , key, " valeus under the list:" , tempList)
        for eachWord in tempList:
            print("word under scan: " , eachWord)
            
            if len(fnlStr)<=0 :
                #print("Here 1 ")
                if re.match(pattern=cPatternCaps , string=eachWord) is None:
                    
                    fnlStr+=eachWord.title()+" "
                else:
                    fnlStr+=eachWord+" "
                    
            else:#when the lenght is greater than Zero already first word is there
                #print("Here 2 ")
                if re.match(pattern=cPatternSmall , string= eachWord) is not None :
                    fnlStr+=eachWord.lower()+" "
                else:
                    fnlStr+=eachWord.lower()+" "
                    
    print("Final String:" , fnlStr)
    fnlStr2 =fnlStr[:len(fnlStr)-1]+"."
    #checkStr= fnlStr2.replace(" " , "")        
    #print("check match[before replacement]: " , re.match(pattern=r'^[A-Z][a-z]*\.$' , string= fnlStr) is  None )
    
    #print("check match[after replacement]: " , re.match(pattern=r'^[A-Z][a-z]*\.$' , string= fnlStr) is  None )
    return fnlStr2
    
                    
                           
            
            
        
        
            
        

#function to extract the word ending with dot
def getLastWordInSentence(sentence):
    lastWordPattern = r'\W\.$'
    cLastWordPattern = re.compile(lastWordPattern)
    lastWord = re.findall(cLastWordPattern , sentence)
    print("The last word in the sentence is: " + lastWord)
    return lastWord
    
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = arrange(sentence)

    fptr.write(result + '\n')

    fptr.close()
