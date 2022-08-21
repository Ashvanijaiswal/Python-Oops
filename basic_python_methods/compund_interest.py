p=int(input("Enter your balance:"))
r=4
a=[p*pow((1+4/100),i) for i in range(1,4) ]
for i in range(1,4):
    print(f"Muldhan after {i} %.2f" %a[i-1])
# generator () vs list comphresion []{}
print(sum(map(lambda i: i*i, range(1000))))
print(sum(i*i for i in range(1,1001)))
