import re
p = re.compile('[a-z]+')
# print(p.match('12 abcd abcd ab jk'))
m=p.match('tempo')
print(m.group())
print(m.start())
print(m.end())
print(m.span())
print(p.search('123 abcd abcd ab jk'))
print(p.findall('abcd abcd ab jk'))
print([i for i in p.finditer('abcd abcd ab jk')])
p = re.compile(r'\d+')
print(p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping'))
s='..112233aavvbb'
p=re.compile(r'(\w+)\1').search(s)
print(p.group(0))
s = r'http://www.google.com/search=ooo-jjj'
p=re.compile(r'(\w)\1\1')
print(p.search(s).group())
print(re.finditer(r'(\w)\1\1',s ))
p=re.compile(r'[^aeiouAEIOU]{1}([aeiouAEIOU]{2,})[^aeiouAEIOU]{1}')
s="Ashvaani"
l=p.finditer(s)
print(l)
m=[x.group() for x in l]
print(m)
# remove duplicate character
st="ashvvannieekkkkkuuumaarrrrr"
print(re.sub(r'(\w)\1+',r'\1',st))
