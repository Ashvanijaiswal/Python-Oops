a=[1,2,3,4]
def is_ugly(a):
    if(is_accesnding(a)):
        return 'Ugly'
    for i in a:
        if(i>len(a)):
            return 'Ugly'
        elif(str(a).count(str(i))>1):
            return 'Ugly'
    else:
        return 'Beautiful'
def is_accesnding(a):
    for i in range(1,len(a)+1):
        if(a[i-1]==1+(i-1)*1):
            continue
        else:
            return False
    return True
print(is_ugly(a))
