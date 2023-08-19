#Remove all duplicate characters in a string
word = input("Enter the string: ")
charList = list(word)
fnlStr=""

for eachChar in charList:
    if eachChar not in fnlStr:
        fnlStr+=eachChar
    else:
        continue

print(fnlStr)