
def find_max(arr,size,k,m,sum):
    if(k<0):
        return -1
    if(size==0):
        return sum
    if((sum+arr[size-1])%m==0):
        return find_max(arr,size-1,k-1,m,sum)
    inc=find_max(arr,size-1,k,m,sum+arr[size-1])
    ex=find_max(arr,size-1,k-1,m,sum)
    return max(inc,ex)

def solve():
    print(find_max(arr,size,k,m,0))

arr=[6,3,7,7,2,4,10]
k=3
m=7
size=len(arr)
print(find_max(arr,size,k,m,0))
