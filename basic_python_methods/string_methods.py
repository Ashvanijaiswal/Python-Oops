s='Ashvani jaiswal \0 Kumar'
print(len(s))
print(s.replace('\0',''))
print(s[7:14])
print(s[:7])
print(s[19:])

print(2 * s)


name='ashvani'
subject='Python'
s1=f'I am {name} I am learning basics of {subject}'
print(s1)

s2='and Java'
print(s1+' '+s2)

c='a'
print(type(c))

string_mul=name.replace('a',name)
print(string_mul)
# print(name.index('basics',4,10))
print('index method throw vallue error exception when not found')
print(name.find('ni'))
print('find method return -1 when no index found')
print(name.find('\n'))
print("".join(reversed(name)))
print(name.upper())
# method-2 reverse string
print(name[::-1])
# method 3 using slice constructo
print(name[slice(-1,-8,-1)])
print(name[-1:-8:-1])

# count() method
s="Python is not only for coder, its for all"
c=s.count("for")
print(c)
