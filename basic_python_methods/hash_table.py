def fun(s):
    for i in range(len(s)):

        if(len(s)!=0):
            yield s[0]
        s=s[1:]

rev=''
for s in fun('Ashvani'):
    rev=s+rev+s
    print(rev)
