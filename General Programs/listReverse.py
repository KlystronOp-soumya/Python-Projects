lis = [1,2,3,4,5,6,7,8]
tempList = []
lis.reverse()
n = len(lis)
"""
 ** Method 1 **
    for i in range( n-1, -1 , -1 ):
        tempList.append(lis[i])
"""
#Method 2
for i in range( 0 , n//2):
    temp = lis[i] 
    lis[i] = lis[n-i-1]
    lis[n-i-1] = temp


print(lis)    