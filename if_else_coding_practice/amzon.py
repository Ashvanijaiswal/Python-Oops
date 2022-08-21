import math
a=[10,20,30,40,50]
rideDuration=70
l=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if(a[i]+a[j]==rideDuration):
            l.append([i,j])
max1=0
for i,j in l:
    if(max(a[i],a[j])>max1):
        max1=max(a[i],a[j])
ni=a.index(max1)
for b in l:
    if(ni in b):
        print(b)
        break

print(i)
print(l)
