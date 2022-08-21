def gcd(x:int,y:int):
    hcf=1
    while(x!=0 and y!=0):
        small=x if(x<y) else y
        big=x if(x>y) else y
        x=big%small
        y=small
    return x if y==0 else y
print(gcd(81,72))
