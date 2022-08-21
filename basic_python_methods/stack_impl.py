def create_stack():
    stack=[]
    return stack
def size(stack):
    return len(stack)
def isEmpty(stack):
    if size(stack)==0:
        return True
    else:
        return False
def push(stack,value):
    stack.append(value)
def pop(stack):
    if isEmpty(stack):
        return
    else:
        return stack.pop()

stack=create_stack()
print(isEmpty(stack))
print(push(stack,10))
print(push(stack,'ash'))
print(isEmpty(stack))
print(pop(stack))
print(stack)
