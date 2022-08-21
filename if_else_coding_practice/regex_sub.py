def multiline():
    while True:
        s=input()
        if not s:
            break
        yield s
l=[]
for value in multiline():
    l.append(value)
print(l)
