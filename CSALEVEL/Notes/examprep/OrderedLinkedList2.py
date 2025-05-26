global Array,StartPointer,FreePointer
Array=[[-1,-1] for n in range(0,10)]
Array=[[-1,n+1] for n in range(0,10)]
Array[9][1]=-1
StartPointer=-1
FreePointer=1


def Add(data:int):
    global Array,StartPointer,FreePointer    
    if StartPointer==-1:
        StartPointer=0
        Array[0][0]=data
        Array[0][1]=-1
        
    else:
        currentPointer=FreePointer
        Array[currentPointer][0]=data
        FreePointer=Array[FreePointer][1]
        previousPointer=StartPointer
        previouspreviousPointer=-1
        while (previousPointer!=-1 and Array[previousPointer][0]<data):
            previouspreviousPointer=previousPointer
            previousPointer=Array[previousPointer][1]
        if previouspreviousPointer==-1:
            Array[currentPointer][1]=StartPointer
            StartPointer=currentPointer
        else:
            Array[previouspreviousPointer][1]=currentPointer
            Array[currentPointer][1]=previousPointer
            
Add(5)
print(Array)
Add(4)
print(Array)
Add(9)
print(Array)
Add(7)
print(Array)
Add(1)
print(Array)
print(StartPointer)