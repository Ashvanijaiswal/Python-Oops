def travserse(arr,curRow,curCol):
    if(curCol>=3):
        return 0
    if(curRow>=3):
        return 1
    print(arr[curRow][curCol])

    if(travserse(arr,curRow,curCol+1)==0):
        return travserse(arr,curRow+1,0)


arr=[[1,2,3],[4,5,6],[7,8,9]]
travserse(arr,0,0)
