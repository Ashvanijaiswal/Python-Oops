def KthCharacterHire2020(s, t, k):
    str=""
    for i in range(1,int(k+1)):
        if(i%2!=0 and len(str)<=int(k)):
            str=str+i*s
        else:
            str=str+i*t
    print(str)
    
    return str[k-1:k]

print(KthCharacterHire2020('a','b',1))