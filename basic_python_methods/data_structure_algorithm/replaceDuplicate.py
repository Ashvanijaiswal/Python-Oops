import re
s="aaabaabbcckkkkdddcazxy"
res=re.sub(r'(\w)\1+',r'\1',s)
print(res)


####################################### simple and easy solution#######
# check last char in string s1 is diffrent than current char of original  s

s="aaabaabbcckkkkdddcazxy"
s1=s[0]
for i in range(1,len(s)):
    if(s1[-1]==s[i]):
        continue
    s1=s1+s[i]

print(s1)
