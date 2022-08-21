def dec_to_bin(n):
    s=''
    if(n==1):
        return '1'
    s=dec_to_bin(n//2)+str(n%2)
    return s


print(dec_to_bin(22))

print('a'>'b')
l=['abc', 'xyz']
print(type(l[0][0]))
