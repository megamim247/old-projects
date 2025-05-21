class Character:
    def __init__(self,PName:str,PXCoordinate:int,PYCoordinate:int):
        #DECLARE XCoordinate, YCoordinate : INTEGER as PRIVATE
        #DECLARE Name : STRING as PRIVATE
        self.__Name=PName
        self.__XCoordinate=PXCoordinate
        self.__YCoordinate=PYCoordinate

    def GetName(self):
         return self.__Name
    
    def GetXCoordinate(self):
        return self.__XCoordinate

    def GetYCoordinate(self):
        return self.__YCoordinate
    
    def ChangePosition(self,PXChange:int,PYChange:int):
        self.__XCoordinate+=PXChange
        self.__YCoordinate+=PYChange

#MAIN
#DECLARE Characters : ARRAY(0,10) of Character
Characters=[Character("",0,0) for n in range(0,10)]
try:
    #DECLARE file : FILE
    #DECLARE Name : STRING
    #DECLARE XCoordinate,YCoordinate : INTEGER
    file=open("Characters.txt","r")
    for n in range(0,10):
        Name=file.readline().strip()
        XCoordinate=file.readline().strip()
        YCoordinate=file.readline().strip()
        print(Name,XCoordinate,YCoordinate)
        Characters[n]=Character(Name,XCoordinate,YCoordinate)
    file.close()
except IOError:
    print("file not real")

#DECLARE CharacterIndex : INTEGER
#DECLARE isinCharacters : BOOLEAN
CharacterIndex=-1
isinCharacters=False
while not(isinCharacters):
    isinCharacters=False
    Name=str(input("enter a name"))
    for n in range(0,len(Characters)):
        if Name==Characters[n].GetName():
            isinCharacters=True
            CharacterIndex=n

Direction=str(input("enter direction"))
while Direction!="W" and Direction!="A" and Direction!="S" and Direction!="D":
    Direction=str(input("incorrect, please reenter direction"))

if Direction=="W":
    Characters[CharacterIndex].ChangePosition(0,1)

if Direction=="A":
    Characters[CharacterIndex].ChangePosition(-1,0)

if Direction=="S":
    Characters[CharacterIndex].ChangePosition(0,-1)

if Direction=="D":
    Characters[CharacterIndex].ChangePosition(1,0)

print(Name,"X=",Characters[CharacterIndex].GetXCoordinate(),"and Y=",Characters[CharacterIndex].GetYCoordinate())
    