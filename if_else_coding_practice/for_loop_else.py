l=[5,1,4,0,2,0]
for i,num in enumerate(l):
    if num==0:
        print(f'Zero found on index {i}')
        break
else:
    print('Zero not found')


n=5
print('%05d'%n)
f=1.2
print('%05.2f'%f)
