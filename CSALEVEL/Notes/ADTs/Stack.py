#initialize stack
stack=[0 for n in range(0,5)]
headpointer=-1

def push(item):
    if headpointer!=len(stack)-1:
        headpointer+=1
        stack[headpointer]=item
    else:
        print("stack full")

def pop():
    if headpointer!=-1:
        item=stack[headpointer]
        return item
    else:
        print("stack empty")