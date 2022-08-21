number_of_bottle=int(input())
size=[]
# for i in range(0,number_of_bottle):
#     ele=int(input())
#     size.append(ele)
# size=[int(input()) for i in range(number_of_bottle)]
size=list(map(int,[input() for _ in range(number_of_bottle)]))
sum=0
for i in size:
    if(i<=1):
        sum+=0.10
    else:
        sum+=0.25
print('Total Deposit is:%.2f'% sum,'$')
