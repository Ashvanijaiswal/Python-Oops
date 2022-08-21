def binary(n):
    # if(n<1):
    #     print(A)
    # else:
    #     A[n-1]=0
    #     binary(n-1)
    #     A[n-1]=1
    #     binary(n-1)
    x=63
    for i in range(0,n+1):
        if(x&(1<<i)!=0):
            print(i)

# A=[0]*5
print(binary(5))
