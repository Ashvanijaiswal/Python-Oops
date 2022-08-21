def reverse(string,rev):
    if(len(string)==0):
        return rev
    return reverse(string[1:],string[0]+rev)

print(reverse("ashvani",""))


print("Hello ",end=",")
print("World")

string="ashvanijaiswal"
strl=""
l=list(string)
print(l)
for i in l:
    strl=strl+l.pop()
    print(i)
print(strl)
