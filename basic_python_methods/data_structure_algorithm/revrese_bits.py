# def singleNumber( A):
#     array=[]
#     for i in range(0,32):
#         for j in A:
#             if((j>>i)&1==1):
#                 array[i]+=1
#     print(array)
# print(singleNumber([0, 0, 0, 1]))

arr=[0]*32
for i in range(10):
    arr[i]=1

print(arr)
