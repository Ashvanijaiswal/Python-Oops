test={
'input':{
'cards':[6,7,8,9,11,22,34,50],
'query':22
},
'output':6
}
#
# print(test['input']['query'])
def binary_search(cards,query,m,l,r,callStack):
    callStack.append(f'binary_search {m} {l} {r}')
    print(callStack)
    if(l>r):

        return -1
    elif(query==cards[m]):

        return m
    elif(query<cards[m]):

        return binary_search(cards,query,(l+m-1)//2,l,m-1,callStack)
    else:
        
        return binary_search(cards,query,(m+1+r)//2,m+1,r,callStack)

s=[6,7,8,9,11,22,34,50]
r=len(s)
l=0
m=(r+l)//2
callStack=[]
print(binary_search(s,45,m,l,r-1,callStack))

# print(binary_search(test['input']['cards'],test['input']['query'],len(test['input']['cards'])//2,0,len(test['input']['cards'])))
