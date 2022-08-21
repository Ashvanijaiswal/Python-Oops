n=int(input("Enter number of decibles:"))
if(n==130):
    print('Jackhammer')
elif(n==106):
    print('Gas lawnmower')
elif(n==70):
    print('Alarm Clock')
elif(n==40):
    print('Quiet Room')
else:
    if(n>130):
        print('Jackhammer','Gas lawnmower','Alarm Clock','Quiet Room')
    elif(130>n>106):
        print('Gas lawnmower','Alarm Clock','Quiet Room')
    elif(106>n>70):
        print('Alarm Clock','Quiet Room')
    elif(70>n>40):
        print('Quiet Room')
    else:
        print('No voice')
