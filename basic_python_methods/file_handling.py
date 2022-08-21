import random,os,six
with open(r'data.txt','r+') as f:
    c=f.read()
    print(c.count('\n'))
# method-2 using generator
num_of_lines=sum(1 for line in open('data.txt'))
print(num_of_lines)

# method-3 using enumrate
my_list=[]
c=0;
with open(r'data.txt','r+') as f:
    my_list=f.readlines()
    f.seek(0)
    for i,line in enumerate(f):
        if(line.count(',')!=2):
            c=i+1
        else:
            break
#             my_list.append(line)
# with open(r'data.txt','w+') as f:
#     f.writelines(my_list)
#
# with open(r'data.txt','r')as f:
#     print(f.readlines())
print(c)
print(my_list[c:])
# os.remove('data.txt')
with open('data.txt','w+')as f:
    f.writelines(my_list[c:])
print(six.MAXSIZE)
