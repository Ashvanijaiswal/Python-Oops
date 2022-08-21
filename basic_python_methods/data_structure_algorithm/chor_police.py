import math
arr=[0,1,1,1,0,1,1,0,0,0]
k=2
police={}
# //key police , val count
chor={}
# key chor, val yes/no

# def max_chor_cathched(arr,k):
#     for i in range(len(arr)):
#         if(arr[i]==0):
#             police[f'P{i}']=0
#         else:
#             chor[f'C{i}']=False
#     print(police)
#     print(chor)
#     count=0
#     for i in police.keys():
#         ind=int(i[1:])
#         # 0,1,1,1,0,1,1,0,0,0]
#         for j in range(k,0,-1):
#             if(ind-j>=0 and arr[ind-j]==1 and police[i]!=1 and chor[f'C{ind-j}']==False):
#                 chor[f'C{ind-j}']=True
#                 police[i]=1
#                 count+=1
#         for j in range(1,k+1):
#             if(ind+j<len(arr) and arr[ind+j]==1 and police[i]!=1 and chor[f'C{ind+j}']==False):
#                 chor[f'C{ind+j}']=True
#                 police[i]=1
#                 count=count+1
#
#     return count
def max_chor_cathched(arr,k):
    police=[]
    chor=[]
    count=0
    for i in range(len(arr)):
        if(arr[i]==0):
            police.append(i)
        else:
            chor.append(i)
    print(police)
    print(chor)
    for i in police:
        for j in chor:
            if(abs(i-j)<=k):
                count+=1
                chor.remove(j)
                break

    return count
print(max_chor_cathched(arr,k))
# print(police)
# print(chor)
