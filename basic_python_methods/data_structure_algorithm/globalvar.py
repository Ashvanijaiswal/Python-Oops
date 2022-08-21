

# Python program showing no need to
# use global keyword for accessing
# a global value

# global variable
a = 4
b = 5

def add():
    for i in range(10):
        c=a+b
        c+=a
    return c



# calling a function
print(add())
