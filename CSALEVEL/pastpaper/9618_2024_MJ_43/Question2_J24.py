class Tree:
    def __init__(self,PTreeName:str,PHeightGrowth:int,PMaxHeight:int,PMaxWidth:int,PEvergreen:str):
        #DECLARE TreeName, Evergreen : STRING PRIVATE
        #DECLARE HeightGrowth, MaxHeight, MaxWidth : INTEGER PRIVATE
        self.__TreeName=PTreeName
        self.__HeightGrowth=PHeightGrowth
        self.__MaxHeight=PMaxHeight
        self.__MaxWidth=PMaxWidth
        self.__Evergreen=PEvergreen
    
    #DECLARE GetTreeName : METHOD
    def GetTreeName(self):
        return self.__TreeName

        #DECLARE GetHeightGrowth : METHOD
    def GetHeightGrowth(self):
        return self.__HeightGrowth
    
        #DECLARE GetMaxHeight : METHOD
    def GetMaxHeight(self):
        return self.__MaxHeight
    
        #DECLARE GetMaxWidth : METHOD
    def GetMaxWidth(self):
        return self.__MaxWidth
    
        #DECLARE GetEvergreen : METHOD
    def GetEvergreen(self):
        return self.__Evergreen

#DECLARE ReadData : FUNCTION returns ARRAY
def ReadData():
    #DECLARE Trees : ARRAY(0,9) of TREE
    #DECLARE count,count2 : INTEGER
    #DECLARE TreeData : LIST
    #DECLARE string : STRING
    count=0  
    TreeData=[None for n in range(0,5)]
    Trees=[Tree("",0,0,0,"") for n in range(9)]
    try:
        file=open("Trees.txt","r")
        for n in file:
            string=""
            count2=0
            for n2 in n:
                string+=n2
                if n2 =="," or n2=="\n":
                    TreeData[count2]=string
                    count2+=1
                    string=""
                    
            Trees[count]=Tree(TreeData[0],TreeData[1],TreeData[2],TreeData[3],TreeData[4])
            count+=1

        file.close()
    except IOError:
        print("file not real")
    
    return Trees


def PrintTrees(tree:Tree):
    if tree.GetEvergreen()=="yes":
        print(tree.GetTreeName(),"has maximum height ",tree.GetHeightGrowth(),"a maximum width ",tree.GetMaxWidth(),"and grows ",tree.GetHeightGrowth(),"cm a year. It does not lose its leaves")
    else:
        print(tree.GetTreeName(),"has maximum height ",tree.GetHeightGrowth(),"a maximum width ",tree.GetMaxWidth(),"and grows ",tree.GetHeightGrowth(),"cm a year. It loses leaves each year")

def ChooseTree():
    #DECLARE Evergreen : STRING PRIVATE
    #DECLARE MaxHeight, MaxWidth, count : INTEGER 
    MaxHeight=int(input("Maximum height"))
    MaxWidth=int(input("Maximum width"))
    Evergreen=str(input("is the tree evergreen"))
    count=0
    #DECLARE Trees : ARRAY(0,9) of TREE
    Trees=[Tree("",0,0,0,"") for n in range(9)]
    for n in Trees:
        if n.GetEvergreen()==Evergreen and n.GetMaxHeight()<MaxHeight and n.GetMaxWidth()<MaxWidth:
            Trees[count]=n.GetTreeName()
            count+=1
    if count==0:
        print("no trees match given parameters")
    else:
        for n in range(0,count):
            PrintTrees(Trees[count])
        treeToBuy=str(input("which tree would you like to buy"))
        heightWhenBought=int(input("height when bought"))
        print("time to grow to max height=",(treeToBuy.GetMaxHeight()-heightWhenBought)/treeToBuy.GetHeightGrowth())

#MAIN
#DECLARE Trees : ARRAY(0,9) of TREE
Trees=[Tree("",0,0,0,"") for n in range(9)]
Trees=ReadData()
PrintTrees(Trees[0])