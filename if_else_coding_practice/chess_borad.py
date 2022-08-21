position=input("Enter position to find color:")
if position[0] in ['a','c','e','g']:
    if int(position[1])%2==0:
        print('white')
    else:
        print('black')
elif position[0] in list('bdfh'):
    if int(position[1])%2==0:
        print('black')
    else:
        print('white')
