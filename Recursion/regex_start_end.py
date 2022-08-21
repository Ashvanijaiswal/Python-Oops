import re
s=input()
k=input()
p=re.compile(k)
st,en=0,0
x=0
flag=True
for i in range(len(s)):
    m=p.search(s)
    old_s=s
    print(s)
    if(m is not None):
        flag=False
        en=x+m.end()-1
        st=x+m.start()
        x=x+st
        print((st,en))
        s=s[m.start()+1:]
    if(old_s==s):
        break
if(flag):
    print(-1,-1)
