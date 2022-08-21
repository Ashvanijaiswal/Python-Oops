C4_freq=261.63
D4_freq=293.66
E4_freq=329.63
F4_freq=349.23
G4_freq=392.00
A4_freq=440.00
B4_freq=493.88
name=input("Enter The two char note name:")
note=name[0]
octav=int(name[1])
if(note=='C'):
    freq=C4_freq
elif(note=='D'):
    freq=D4_freq
elif note=='E':
    freq=E4_freq
elif note=='F':
    freq=F4_freq
elif note=='G':
    freq=G4_freq
elif note=='A':
    freq=A4_freq
elif note=='B':
    freq=B4_freq

freq=freq/(2**(4-octav))
print(f"The frequncy of {name} is:%.2f"%freq)
