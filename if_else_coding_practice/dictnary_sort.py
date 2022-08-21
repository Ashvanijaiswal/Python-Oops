s = input()
d={}
s=''.join(sorted(s))
l=[]
for i in s:
    if i not in l:
        l.append(i)
        d[i]=s.count(i)
res=sorted(d.items(),reverse=True,key=lambda x:x[1])
res=res[0:3]
print(res)
