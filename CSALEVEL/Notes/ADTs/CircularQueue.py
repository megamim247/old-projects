queue=[0 for n in range(0,5)]
frontPointer=-1
endPointer=-1
def enqueue(item):
    global frontPointer, endPointer, queue
    if endPointer == len(queue)-1:
        if frontPointer==-1 or frontPointer==0:
            print("Queue is full")
            return -1
        else:
            endPointer = 0
            queue[endPointer] = item
            print(f"Item added: {item}")
    else:
        if endPointer == frontPointer and endPointer != -1:
            print("Queue is full")
            return -1
        else:
            endPointer += 1
            queue[endPointer] = item
            print(f"Item added: {item}")

def dequeue():
    global frontPointer, endPointer, queue
    if endPointer == -1:
        endPointer=0

    if frontPointer == len(queue)-1: 
        if endPointer == len(queue)-1:
            print("Queue is empty")
            return -1
        else:
            item= queue[frontPointer]
            print(f"Item removed: {item}")
            frontPointer = 0

    if frontPointer == endPointer-1:
        print("Queue is empty")
        return -1
    else:
        frontPointer += 1
        item= queue[frontPointer]
        print(f"Item removed: {item}")

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