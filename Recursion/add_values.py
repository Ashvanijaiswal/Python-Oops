def add_value():
    sum=0.0
    val=input()
    if val =="":
        return 0
    else:
        sum=sum+float(val)
        return sum+add_value()

print(add_value())
