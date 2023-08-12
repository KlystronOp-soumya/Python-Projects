#Script to check a number is Krishanmurthy number
"""
145 -> 1! + 4! + 5! == 145
"""
num = int(input("Enter a number: "))
temp_num = num #to keep a reference

#Step1: extract the digits from the number
#Step2: count the factorial
#Step3: Add the factorials
#Step4: Validate with the actual number

#Initializing
sum=0
fact = 1 
fact_lc = 1 #the loop counter
while(temp_num != 0):
    #get the remainder
    rem =  temp_num%10
    #calculate the factorial
    while(fact_lc <= rem): #inner while loop to calculate the factorial of the remainder 
        fact*=fact_lc
        fact_lc+=1
    
    #outside of the inner while loop
    print('{}! = {}'.format(rem , fact))
    sum+=fact
    temp_num = temp_num//10

    #reset the values for the while loop
    fact_lc=1 
    fact = 1

if(sum == num):
    print(num , " is Krishnamurthy Number")
else:
    print(num , " is not a Krishnamurthy Number")


