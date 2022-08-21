def allPermutaion(s,l,r):
    if(l==r):
        print(s)
        return
    for i in range(0,len(s)):
        s=swap(s,i,l)
        allPermutaion(s,l+1,r)
        s=swap(s,i,l)
def swap(s,i,j):
    l=list(s)
    temp=s[i]

    l[j]=temp
    return str(l)


s="abc"
allPermutaion(s,0,2)
