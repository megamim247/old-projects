def AddNode(): 
    #DECLARE data,CurrentPointer : INTEGER
    Data=int(input("enter data"))
    global ArrayNodes,RootPointer,FreeNode #BYREF
    ArrayNodes[FreeNode][0]=-1
    ArrayNodes[FreeNode][1]=Data
    ArrayNodes[FreeNode][2]=-1
    if RootPointer==-1:
        RootPointer=0
    else:
        CurrentPointer=RootPointer
        while CurrentPointer!=-1:
            TurnedRight=False
            if ArrayNodes[1]>Data:
                TurnedRight=True
                CurrentPointer=ArrayNodes[CurrentPointer][2]
            else:
                TurnedRight=False
                CurrentPointer=ArrayNodes[CurrentPointer][0]

        ArrayNodes[CurrentPointer]=Data
        if TurnedRight:
            ArrayNodes[CurrentPointer][0]=FreeNode
        else:
            ArrayNodes[CurrentPointer][2]=FreeNode
    FreeNode+=1

def printAll():
    global FreeNode,ArrayNodes #BYREF
    for n in range(0,FreeNode):
        print(ArrayNodes[n][0]," ",ArrayNodes[n][1]," ",ArrayNodes[n][2])

def InOrder(Root:int):
    global ArrayNodes
    if ArrayNodes[Root][0]!=-1:
        InOrder(ArrayNodes[Root][0])
    print(ArrayNodes[Root][1])
    if ArrayNodes[Root][2]!=-1:
        InOrder(ArrayNodes[Root][2])

#MAIN
global ArrayNodes,RootPointer,FreeNode #BYREF
#DECLARE ArrayNodes : ARRAY(0,19)(0,2) of INTEGER
ArrayNodes=[[-1,-1,-1] for n in range(0,20)]
#DECLARE RootPointer,FreeNode : INTEGER
RootPointer=-1
FreeNode=0
