global Array,FreePointer,RootPointer
Array=[[-1,-1,-1] for n in range(0,10)]
RootPointer=-1
FreePointer=0
def Add(data:int):
    global Array,FreePointer,RootPointer
    if RootPointer==-1:
        RootPointer=0
        Array[0][1]=data
        FreePointer+=1
    else:
        if FreePointer<10:
            currentPointer=RootPointer
            previousPointer=0
            Array[FreePointer][1]=data
            while currentPointer!=-1:
                previousPointer=currentPointer
                if Array[currentPointer][1]<data:
                    currentPointer=Array[currentPointer][2]
                    TurnedRight=True
                else:
                    currentPointer=Array[currentPointer][0]
                    TurnedRight=False
            if TurnedRight:
                Array[previousPointer][2]=FreePointer
            else:
                Array[previousPointer][0]=FreePointer
            FreePointer+=1

def InOrder(Root):
    if Array[Root][0]!=-1:
        InOrder(Array[Root][0])
    
    print(Array[Root][1])

    if Array[Root][2]!=-1:
        InOrder(Array[Root][2])

    return "NIGGA"

Add(5)
print(Array)
Add(3)
print(Array)
Add(4)
Add(6)
Add(8)
Add(9)
Add(7)
Add(1)
Add(2)
print(Array)
print(InOrder(RootPointer))