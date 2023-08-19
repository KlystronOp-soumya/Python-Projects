# ENter a  character to check whether is a lower case , upper case , digit or speciak character
SPECIAL_CHARS=['~' , '`','\\' , '//' , ';', '\'' , '\"' , '*' , '&'] #add the other special characters
charc = input("Enter a character: ")

if (ord(charc) >= 97 and ord(charc) <= 122 ):
    print("lower")
elif (ord(charc) >= 65 and ord(charc) <= 90) :
    print("upper")
elif(ord(charc) >=49 and ord(charc) <=57 ) :
    print("digit")
elif charc in SPECIAL_CHARS:
    print("Special")
else:
    print("Unknown")
