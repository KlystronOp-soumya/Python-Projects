#Program to count #upper case , #lower case , digits,space,words

line = input("Enter a line: ")

#an brute force algo
countWord=0
countUpper=0
countLower=0
countDigit=0
countSpace=0
words=line.split(' ')

countWord = len(words)
countSpace = countWord -1 
for eachWord in words:
    for eachChar in eachWord:
        if eachChar.isupper():
            countUpper+=1
        elif eachChar.islower():
            countLower+=1
        elif eachChar.isdigit():
            countDigit+=1
        else:
            continue

print("The line \"{}\" containes :\n Upper Case Letters:{}\n Lower case letters:{}\n Spaces:{}\n Words:{}\n Digits: {}".format(line , countUpper , countLower , countSpace , countWord , countDigit))
