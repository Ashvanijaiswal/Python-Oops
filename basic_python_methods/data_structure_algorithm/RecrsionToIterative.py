def factorial(n):
    stack=[]
    result=None
    stack.append(('call',n))
    while(stack):
        action,data=stack.pop()
        if(action=='call'):
            n=data
            if(data==1):
                result=1
            else:
                stack.append(('Resume',n))
                stack.append(('call',n-1))
        elif(action=='Resume'):
            n=data
            fact=n*result
            result=fact
    return result

if __name__=='__main__':
    f=factorial(3)
    print(f)
