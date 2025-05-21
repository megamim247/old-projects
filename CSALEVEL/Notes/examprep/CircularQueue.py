global Array,HeadPointer,TailPointer,NumInQueue
Array=[0 for n in range(0,10)]
HeadPointer=0
TailPointer=0
NumInQueue=0
def Enqueue(data:int):
    global Array,HeadPointer,TailPointer,NumInQueue
    if NumInQueue<10:
        if TailPointer<10:
            Array[TailPointer]=data
            TailPointer+=1
            NumInQueue+=1
        else:
            TailPointer=0
            Array[TailPointer]=data
            NumInQueue+=1
    else:
        print("Queue full")

def Dequeue():
    global Array,HeadPointer,TailPointer,NumInQueue
    if NumInQueue>0:
        if HeadPointer<10:
            data=Array[HeadPointer]
            HeadPointer+=1
            NumInQueue-=1
        else:
            HeadPointer=0
            data=Array[HeadPointer]
            NumInQueue-=1
        print(data)
    else:
        print("Queue empty")

def ArPrint():
    global Array,HeadPointer,TailPointer,NumInQueue
    for n in range(HeadPointer,TailPointer):
        print(Array[n],end=",")
    print("")
    
Enqueue(1)
Enqueue(2)
Enqueue(3)
Enqueue(4)
Enqueue(5)
Enqueue(6)
Enqueue(7)
Enqueue(8)
Enqueue(9)
Enqueue(10)
Enqueue(11)
ArPrint()
Dequeue()
Dequeue()
Dequeue()
ArPrint()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
ArPrint()