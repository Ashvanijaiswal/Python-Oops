l=[1,2,3,4,5]

def fun(l):
    if(len(l)==0):
        return
    print(l[0])
    fun(l[1:])

fun(l)

def fun_end(l):
    if(len(l)==0):
        return
    fun_end(l[1:])
    print(l[0])
print('#############################')
fun_end(l)
