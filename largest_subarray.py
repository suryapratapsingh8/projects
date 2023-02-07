l=list(map(int,input().split()))

le=2
for i in range(2,len(l)):
    if l[i-2]+l[i-1]==l[i]:
        
        le=le+1 
    else:
        break
print(le)
