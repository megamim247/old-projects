class node:
    def __init__(self,Pdata:int,PnextNode:int):
        #DECLARE data,nextNode : INTEGER
        self.data=Pdata
        self.nextNode=PnextNode

#DECLARE outputNodes : PROCEDURE
def outputNodes(linkedList:list,startPointer:int):
    while startPointer!=-1:
        print(linkedList[startPointer].data)
        startPointer=linkedList[startPointer].nextNode

#DECLARE addNode : FUNCTION returns BOOLEAN
def addNode():
    #DECLARE new,currentPointer,prevousEmpty : INTEGER
    global linkedList,startPointer,emptyList
    new=int(input("enter data:"))
    currentPointer=startPointer
    if emptyList!=-1:
        previousEmpty=emptyList
        emptyList=linkedList[emptyList].nextNode
        linkedList[previousEmpty]=node(new,-1)
        while currentPointer!=-1:
            currentPointer=linkedList[currentPointer].nextNode
        linkedList[currentPointer].nextNode=previousEmpty
        return True
    else:
        return False



#MAIN
#DECLARE linkedList : ARRAY(0,9) of node GLOBAL
#DECLARE startPointer,emptyList : INTEGER GLOBAL
global linkedList,startPointer,emptyList
linkedList=[node(0,n) for n in range(0,10)]
linkedList=[node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
startPointer=0
emptyList=5

#DECLARE added : BOOLEAN
outputNodes(linkedList,startPointer)
added=addNode()
if added:
    print("item was added successfully")
else:
    print("list full")
outputNodes(linkedList,startPointer)

