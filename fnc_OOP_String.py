
from collections import Counter
import re

""" A demo funtion is written if re not used """
""" def replaceWithString(para,special1):
    temp=""
    for eachChar in para:
        if eachChar not in special1:
            temp+=eachChar
        else:
            temp+=" "
    print(temp.strip())
    return temp.strip() """
            
def stringmethod(para,special1,special2,list1,strf):
    #word1=replaceWithString(para,special1)
    flag=True
    pattern = "["+special1+"]" #converting the string into the pattern
    word1 = re.sub(pattern,"",para)
    #word1=word1[::-1]
    print()
    temp = word1[:70] #getting the first 70 characters
    #print(temp)
    rword2=' '.join(reversed([eachString[::-1] for eachString in temp.split(" ")]))
    print(rword2)
    rword2=rword2.replace(" ","")
    #print(rword2)
    rword3=special2.join([eachChar for eachChar in rword2])
    print(rword3)
    
    for eachWord in list1:
        if eachWord not in word1.split():
            flag=False
            print("Every string in {} were not present".format(list1))
            break
        else:
            flag=True
    
    if(flag):
        print("Every string in {} were present".format(list1))

    print(word1.split()[:20])
    less_wrd=[]
    counted = Counter(word1.split())
    for eachWord in word1.split():
        if counted[eachWord] < 3:
            if eachWord not in less_wrd:
                less_wrd.append(eachWord)
    
    print(less_wrd[len(less_wrd)-20:])
    
    print(word1.rfind(strf))

if __name__ == '__main__':
    para = input()

    spch1 = input()
    
     
    spch2 = input()
    
    
    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = input()
        qw1.append(qw1_item)
    
    strf = input() 
    stringmethod(para,spch1,spch2,qw1,strf)

"""
wd=[]
for i in range(len(para)):
wd.append(para[i])
word1=[]
for i in wd:
if i not in special1:
word1.append(i)
word1=””.join(word1)
w=[]
for i in range(0,70):
w.append(word1[i])
word2=””.join(w)
word2=word2[::-1]
print(word2)
word3=word2.split()
word3=””.join(word3)
word3a=[]
for i in word3:
word3a.append(i)
word3b=special2.join(word3a)
print(word3b)
count=0
for i in list1:
if i in para:
count=count+1
if count==len(list1):
print(“Every string in”,list1,”were present”,sep=” “)
else:
print(“Every string in”,list1,”were not present”,sep=” “)
nword1=word1.split()
nw2=[]
for i in range(20):
nw2.append(nword1[i])
print(nw2)
dic={}
word1a=word1.split()
for i in word1a:
dic[i]=word1a.count(i)
lis1=[]
for i in dic:
if dic[i]<3:
lis1.append(i)
lis2=[]
for i in range(len(lis1)-1,len(lis1)-21,-1):
lis2.append(lis1[i])
print(lis2[::-1])
print(word1.rindex(strfind))
"""