import math,time
x=int(input())
s=input().split(' ')
a=[int(i) for i in s]
print(time.ctime())
def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
            break
    return True

def fun(n):
    while n>1:
        for i in range(2,n+1):
            if(isprime(n)):
                yield n
                n=1
                break

            if(n%i==0):
                n=n//i
                yield n
                break
sum1=0
for i in a:
    l=[]
    for num in fun(i):
        l.append(num)
    if(len(l) in [0,1]):
        sum1=sum1+1
    else:
        last=l[-2]
        l=l[:-2]
        sum1+=sum(l)+last+1+i
print(sum1)
print(time.ctime())
