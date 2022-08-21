p=0
for i in range(0,9):
    if(i<=4):

        for j in range(0,9):
            if(j==i or j==8-i):
                print(f'{i}',end="")
            else:
                print(" ",end="")

        print()
    else:
        p=p+2
        for j in range(0,9):
            if(j==i or j==8-i):
                print(f'{i-p}',end="")
            else:
                print(" ",end="")
        print()
