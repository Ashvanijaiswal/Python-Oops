import numpy as np
a=np.random.randint(1,size=5)
print(a)

q=[[1,2,100],[2,5,100],[3,4,100]]

for i,j,sum in q:
    a[i-1:j]=np.apply_along_axis(lambda x:x+sum,0,a[i-1:j])
print(a.max())
print(a[a.argmax(axis=0)])
print(a)
l=5*[0]
print(l)
