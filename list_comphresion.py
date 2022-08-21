if __name__ == '__main__':
    n=int(input())

    stud=[]
    for i in range(n):
        name=str(input())
        grade=float(input())
        stud.append([name,grade])
    
grades=[]
for i in stud:
    grades.append(i[1])
order=sorted(set(grades))
print(order)
names=[]
for i in stud:
    if i[1]==order[1]:
         names.append(i[0])
names.sort()
for i in names:
    print(i)