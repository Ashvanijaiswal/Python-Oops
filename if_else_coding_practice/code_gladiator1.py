import math
x=int(input())
m=[]
def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
            break
    return True
def recursive(n,l):
    print(n)

    if(n==1 or isprime(n)):

        return l
    for i in range(2,n+1):
        if(n%i==0):
             l.append(n//i)
             recursive(n//i,l)
             print(l)
             break


    return l
# print(recursive(x,m))

def factorial(n):
    if(n==0 or n==1):
        return 1
    fact=n*factorial(n-1)
    return fact



def factorial2(n,accum):
    print(accum)
    if(n==1 or n==0):
        return accum

    return factorial2(n-1,accum*n)


# print(factorial(7))
print(factorial2(7,1))
