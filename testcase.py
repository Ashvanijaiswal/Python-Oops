for i in range(1,100):
    if(len(str(i))==1):
        print("TC00"+str(i))
    elif(len(str(i))==2):
        print("TC0"+str(i))
    else:
        print("TC"+str(i))

