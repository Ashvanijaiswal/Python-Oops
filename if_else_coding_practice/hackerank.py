l=1000000000*[0]
queries=[[1,2,100],[2,5,100],[3,4,100]]
def su(x):
    return sum1+x
for i,j,sum1 in queries:
    if(i>=1):
        l[i-1:j]=list(map(su,l[i-1:j]))


print(sum(i**2 for i in range(1000)))
