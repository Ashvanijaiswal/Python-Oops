
def noOfWays(r,c):
    if(r==1 or c==1):
        return 1
    return noOfWays(r-1,c)+noOfWays(r,c-1)


r=4
c=4
print(noOfWays(r,c))
