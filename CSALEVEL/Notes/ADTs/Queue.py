queue1 = [0 for i in range(10)] 
 
 
 
frontpointer = -1 
endpointer = -1 
 
def enqueue(queue, item): 
    global frontpointer, endpointer 
    if frontpointer == len(queue)-1: 
        print("queue full") 
        return -1 
    else: 
        frontpointer = frontpointer + 1 
        queue[frontpointer] = item 
        print(f"item added {item}") 
 
def dequeue(queue): 
    global frontpointer, endpointer 
    if endpointer == -1: 
        print("queue empty") 
        return -1 
    else: 
        item = queue[endpointer] 
        endpointer +=1 
        return item 
 