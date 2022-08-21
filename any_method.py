a,b,c=2,0,'ok'
conds=[a==1,
        b==2,
        c=='ok']
# it will check if any of the value is true then it return true
if any(conds):
    print('Yes!')
else:
    print('No!')
print('Yes!' if any(conds) else 'No')
