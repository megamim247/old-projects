queue=[0 for n in range(0,5)]
frontPointer=-1
endPointer=-1
queuelength=0
def enqueue(item):
    global queue,frontPointer,endPointer,queuelength
    if queuelength<len(queue)-1:
        endPointer+=1
        if endPointer ==len(queue):
            endPointer=0
        queue[endPointer]=item
        queuelength+=1
        print("item added",item)
    else:
        print("queue full")

def dequeue():
    global queue,frontPointer,endPointer,queuelength
    if queuelength!=0:
        frontPointer+=1
        if frontPointer ==len(queue):
            frontPointer=0
        item=queue[frontPointer]
        queuelength-=1
        print("item removed",item)
    else:
        print("queue empty")

enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
dequeue()
dequeue()
dequeue()
enqueue(5)
enqueue(6)
print(queue)
enqueue(7)
enqueue(8)
print(queue)
dequeue()
dequeue()
enqueue(9)
enqueue(10)
print(queue)