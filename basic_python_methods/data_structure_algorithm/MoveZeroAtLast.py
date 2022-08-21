def moveZero(arr):
    lPointer=0
    # 0 0 2 3 4 6
    for i in range(0,len(arr)):
        if(arr[i]!=0):
            [arr[i],arr[lPointer]]=[arr[lPointer],arr[i]]
            lPointer+=1

    return arr

arr=[0,3,5,0,4,0,7,0,6]
print(moveZero(arr))
