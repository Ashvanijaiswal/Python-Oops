a=float(input("Enter value for a:"))
b=float(input("Eneter value for b:"))
c=float(input("Enetr value for c:"))
descrimant=b**2-4*a*c
if(descrimant>0):
    print("there are two roots and the roots are:")
    x=(-1*b+descrimant)/(2*a)
    y=(-1*b-descrimant)/(2*a)
    print(f'x=%07.3f'%x)
    print(f'y=%07.3f'%y)
elif descrimant<0:
    print("There are no reals roots")
else:
    print("There is only one root")
    root=-1*b/(2*a)
    print(f'root={root}')


# print(x,y)
