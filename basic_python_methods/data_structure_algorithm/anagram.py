s1='abcd'
s2='bdac'
l=[0]*26
for i in s1:
    l[ord(i)-97]=l[ord(i)-97]+1
for j in s2:
    l[ord(i)-97]=l[ord(i)-97]-1;

print(True if(sum(l)==0) else False)

a=(1,2,3,4)
b=(2,3,0)
