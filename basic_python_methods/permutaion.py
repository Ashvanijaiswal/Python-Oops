import re
s='abcacacbdbacbacb'
f='abc'
count=0
f_sorted=sorted(f)
for i in range(0,len(s)):
    x=s[:len(f)]
    if(f_sorted==sorted(x)):
        count=count+1
    s=s[1:]

print(count)


def uniary_operator(number):
    number+=1
    return number
print(uniary_operator(9))
