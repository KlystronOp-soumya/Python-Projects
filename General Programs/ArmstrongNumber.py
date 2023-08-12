#Script to check the Armstrong Number
"""
A positive integer of n digits is called an Armstrong number of order n (order is the number of digits) if. 

abcd… = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + 
Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

Input : 120
Output : No
120 is not a Armstrong number.
1*1*1 + 2*2*2 + 0*0*0 = 9

Input : 1253
Output : No
1253 is not a Armstrong Number
1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723

Input : 1634
Output : Yes
1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634
"""
from math import pow as power
num = int (input("Enter the number: "))

#Step1 : count the total number of digits there are multiple ways

digit_count = 0
temp_num = num
sum=0
while(temp_num):
    digit_count+=1
    temp_num=temp_num//10

print("Digit count" , digit_count)
#reassign
temp_num = num

while(temp_num):
    rem = temp_num%10
    pos= power(rem , digit_count)
    sum+=pos
    print(f'current digit:{rem}^{digit_count}:{pos}')
    temp_num//=10

if(sum == num):
    print(f'{num} is Armstrong')
else:
    print("not armstrong")


