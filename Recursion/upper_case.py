import re

# def upper_case_index(s):
#     l=[]
#     for i,c in enumerate(s):
#         if(c.isupper()):
#             l.append(i)
#     return l
# print(upper_case_index("HellOMe"))

def upper_case_index(s):
    l=[]
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i,c in enumerate(s):
        if(c in upper):
            l.append(i)
    return l
# print(upper_case_index("HellOMe"))

def upper_case_index_reg(s):
    l=[]
    p=re.compile(r'[A-Z]')
    for i in range(len(s)):
        m=p.search(s)
        # print(m.group())
        if(m is not None):
            l.append(i+m.start())
            s=s[m.start()+1:]
    return l
print(upper_case_index_reg('HellOMe'))

def recursion_method(s):
    if(len(s)==0):
        return
    print(s[0] if(s[0].isupper()) else "",end="")
    recursion_method(s[1:])

recursion_method('HellOMe')



def print_number(n):
    if(n==0):
        return
    print(n)
    print_number(n-1)
print_number(5)


def prime_number(n,i):
    if(i>=n/2):
        return True
    if(n%i==0):
        return False

    flag=prime_number(n,i+1)
    return flag

print(prime_number(41,2))
