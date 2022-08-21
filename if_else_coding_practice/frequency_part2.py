C4_freq=261.63
D4_freq=293.66
E4_freq=329.63
F4_freq=349.23
G4_freq=392.00
A4_freq=440.00
B4_freq=493.88
limit=1
freq=float(input("Enter a frequncy:"))
if C4_freq-1<=freq<=C4_freq+1:
    name='C4'
elif D4_freq-1<=freq<=D4_freq+1:
    name='D4'
elif E4_freq-1<=freq<=E4_freq+1:
    name='E4'
elif F4_freq-1<=freq<=F4_freq+1:
    name='F4'
elif G4_freq-1<=freq<=G4_freq+1:
    name='G4'
elif A4_freq-1<=freq<=A4_freq+1:
    name='A4'
elif B4_freq-1<=freq<=B4_freq+1:
    name='B4'
else:
    name=""


if(name==""):
    print("Not related to any note")
else:
    print(f'This frequncy {freq} belongs to ',name)
