r = int(input())
c = int(input())
l2=list()
for i in range(0,r):
    l1 = list(map(int, input("Enter multiple values: ").split()))
    l2.append(l1)

print(l2)

l3=l2.copy()

print(l3)


