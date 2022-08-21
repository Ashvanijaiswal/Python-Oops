magnitude=float(input("Enetr the magnitude:"))
dec=''
if(magnitude<2.0):
    desc='Micro'
elif 2<=magnitude<3:
    desc='Very Minor'
elif 3<=magnitude<4:
    desc='Minor'
elif 4<=magnitude<5:
    desc='Light'
elif 5<=magnitude<6:
    desc='Moderater'
elif 6<=magnitude<7:
    desc='Strong'
elif 7<=magnitude<8:
    desc='Major'
elif 8<=magnitude<10:
    desc='Great'
elif magnitude>=10:
    desc='Meteoric'

print(f'{magnitude} earthquqke is considered to be {desc}')
print(f'%.2f'%magnitude)
