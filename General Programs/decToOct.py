def decToOct(n):
    print(oct(n))


# Python3 program to convert decimal
# number to octal number
 
# function to calculate the octal value of the given
# decimal number
 
 
def decimaltoOctal(deciNum):
 
    # initializations
    octalNum = 0
    countval = 1
    dNo = deciNum
 
    while (deciNum != 0):
 
        # decimals remainder is calculated
        remainder = deciNum % 8
 
        # storing the octalvalue
        octalNum += remainder * countval
 
        # storing exponential value
        countval = countval * 10
        deciNum //= 8
 
    print(octalNum)