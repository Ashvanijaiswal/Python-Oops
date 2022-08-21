# print(int("1111",2))
# print(bin(15).lstrip('0b'))

s='ashvani'
print(s[::-1])
k=slice(-1,-8,-1)
print(s[k])
print(''.join(reversed(s)))

def rev(s):
    p=''
    for i in s:
        p=i+p
    print(p)
rev(s)


def rev1(s):
    p=''
    for i in range(len(s)-1,-1,-1):
        p=p+s[i]
    print(p)
rev1(s)

def rev_rec(s):
    if(len(s)==0):
        return
    rev_rec(s[1:])
    print(s[0],end='')
rev_rec(s)
