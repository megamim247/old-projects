class Node:
    def __init__(self,PLeftPointer,PData,PRightPointer):
        #DECLARE RightPointer,Data,LeftPointer : INTEGER PRIVATE
        self.__RightPointer=PRightPointer
        self.__Data=PData
        self.__LeftPointer=PLeftPointer
    
    #DECLARE GetLeft : FUNCTION return INTEGER
    def GetLeft(self):
        return self.__LeftPointer
    
    #DECLARE GetData : FUNCTION return INTEGER
    def GetData(self):
        return self.__Data
    
    #DECLARE GetRight : FUNCTION return INTEGER
    def GetRight(self):
        return self.__RightPointer
    
    #DECLARE SetLeft : FUNCTION return INTEGER
    def SetLeft(self):
        return self.__LeftPointer
    
    #DECLARE SetData : FUNCTION return INTEGER
    def SetData(self):
        return self.__Data
    
    #DECLARE SetRight : FUNCTION return INTEGER
    def SetRight(self):
        return self.__RightPointer
    
class TreeClass:
    def __init__(self):
        #DECLARE Tree : ARRAY(0,20) of Node PRIVATE
        #DECLARE FirstNode, NumberNodes : INTEGER PRIVATE
        self.__Tree=[Node(-1,-1,-1) for n in range(0,20)]
        self.__FirstNode=-1
        self.__NumberNodes=0
    
    #DECLARE InsertNode : FUNCTION
    def InsertNode(self,PNewNode:Node):
        if self.__NumberNodes==0:
            self.__FirstNode==0
            self.__Tree[0]=PNewNode
            self.__NumberNodes=1
        else:
            self.__Tree[self.__NumberNodes]=PNewNode
            curPointer=self.__FirstNode
            while curPointer!=-1:
                previousPointer=curPointer
                if PNewNode.GetData()>self.__Tree[curPointer].GetData():
                    curPointer=self.__Tree[curPointer].GetRight()
                    TurnedLeft=False
                else:
                    curPointer=self.__Tree[curPointer].GetLeft()
                    TurnedLeft=True
            if TurnedLeft:
                self.__Tree[previousPointer].SetLeft(self.__NumberNodes)
            else:
                self.__Tree[previousPointer].SetRight(self.__NumberNodes)
            self.__NumberNodes+=1
    
    def OutputTrees(self):
        for n in range(0,self.__NumberNodes):
            print(self.__Tree[n].GetRight(),self.__Tree[n].GetData(),self.__Tree[n].GetLeft)


TheTree=TreeClass()
TheTree.InsertNode(Node(-1,10,-1))
TheTree.InsertNode(Node(-1,11,-1))
TheTree.InsertNode(Node(-1,5,-1))
TheTree.InsertNode(Node(-1,1,-1))
TheTree.InsertNode(Node(-1,1,-1))
TheTree.InsertNode(Node(-1,20,-1))
TheTree.InsertNode(Node(-1,15,-1))
TheTree.OutputTrees()