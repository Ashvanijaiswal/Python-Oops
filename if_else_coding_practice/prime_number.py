import math

def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
            break
    return True
print(isprime(17))
