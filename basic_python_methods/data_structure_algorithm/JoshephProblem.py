def solve_josheph(n,k,callStack):
    callStack.append(f'solve_josheph {n} {k}')
    print(callStack)
    if(n==1):
        callStack.pop()
        print(callStack)
        return 0
    callStack.pop()
    print(callStack)
    return (solve_josheph(n-1,k,callStack)+k)%n

n=5
k=3
callStack=[]
print(solve_josheph(n,k,callStack))
