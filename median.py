'''import statistics
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=l1+l2
l3.sort()
print(statistics.median(l3))

'''
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=l1+l2
l3.sort()
k=len(l3)
m=k//2
if k&1==0:
    s=l3[m-1]+l3[m]
    print(s/2)
else:
    print(l3[m])