def fib(n):
    if(n<2):
        return n
    if is_computed[n]:
        return F[n]
    F[n]=fib(n-1)+fib(n-2)
    is_computed[n]=True
    return F[n]

def f(n):
    F[0]=0
    F[1]=1
    for i in range(2,n+1):
        F[i]=F[i-1]+F[i-2]
    return F[n]


F=[0]*11
# is_computed=[False]*11
print(f(10))
print(F)
# print(is_computed)
