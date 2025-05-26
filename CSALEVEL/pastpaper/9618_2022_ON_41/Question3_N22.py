#DECLARE SearchValue : FUNCTION returns INTEGER
def SearchValue(Root:int,ValueToFind:int):
    if Root==-1:
        return -1
    else:
        if ArrayNodes[Root][1]==ValueToFind:
            return Root
        else:
            if ArrayNodes[Root][1]==-1:
                return -1
    if ArrayNodes[Root][1]>ValueToFind:
        return SearchValue(ArrayNodes[Root][0],ValueToFind)
    if ArrayNodes[Root][1]<ValueToFind:
        return SearchValue(ArrayNodes[Root][2],ValueToFind)

#DECLARE PostOrder : FUNCTION returns INTEGER
def PostOrder(Root:int):
    if Root!=-1:
        PostOrder(ArrayNodes[Root][0])
        PostOrder(ArrayNodes[Root][2])
        print(ArrayNodes[Root][1])


#MAIN
#DECLARE ArrayNodes : ARRAY[0:19,0:2] OF INTEGER GLOBAL
global ArrayNodes
ArrayNodes=[[-1,-1,-1] for n in range(0,20)]
ArrayNodes[0]=[1,20,5]
ArrayNodes[1]=[2,15,-1]
ArrayNodes[2]=[-1,3,3]
ArrayNodes[3]=[-1,9,4]
ArrayNodes[4]=[-1,10,-1]
ArrayNodes[5]=[-1,58,-1]
#DECLARE FreeNode,RootPointer : INTEGER
FreeNode=6
RootPointer=0
#DECLARE Index : INTEGER
Index=SearchValue(RootPointer,15)
if Index!=-1:
    print("Value found at ",Index)
else:
    print("Value not found")
PostOrder(RootPointer)