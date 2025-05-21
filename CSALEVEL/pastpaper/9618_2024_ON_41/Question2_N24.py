class Horse:
    def __init__(self,PName:str,PMaxFenceHeight:int,PPercentageSuccess:int):
        #DEFINE Name: STRING PRIVATE
        #DEFINE MaxFenceHeight, PercentageSuccess : INTEGER PRIVATE
        
        self.__Name=PName
        self.__MaxFenceHeight=PMaxFenceHeight
        self.__PercentageSuccess=PPercentageSuccess
    
    def GetName(self):
        return self.__Name
    
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight
    
    def Success(self):
        pass

class Fence:
    def __init__(self,PHeight,PRisk):
        #DECLARE Height,Risk : INTEGER PRIVATE
        self.__Height=PHeight
        self.__Risk=PRisk
    
    def GetHeight(self):
        return self.__Height
    
    def GetRisk(self):
        return self.__Risk

#MAIN
#DECLARE Horses : ARRAY(0,2) of Horse
Horses=[Horse("",0,0) for n in range(0,2)]
Horses[0]=Horse("Beauty",0,0)
Horses[1]=Horse("Jet",0,0)
for n in Horses:
    print(n.GetName())

#DECLARE Course : ARRAY(0,4) of Fence
#DECLARE height,risk : INTEGER
Course=[Fence(0,0) for n in range(0,4)]

for n in range(0,5):
    height=int(input("enter max height"))
    risk=int(input("enter maximum risk"))
    while height<70 or height>180 or risk<1 or risk>5:
        height=int(input("enter max height"))
        risk=int(input("enter maximum risk"))
    Course[n]=Fence(height,risk)


