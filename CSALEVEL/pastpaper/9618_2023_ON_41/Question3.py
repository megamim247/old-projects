class Character:
    def __init__(self,PName:str,PXPosition:int,PYPosition:int):
        #DECLARE Name : STRING
        #DECLARE XPostition, YPosition : INTEGER
        self.__XPosition=PXPosition
        self.__YPosition=PYPosition
        self.__Name=PName
        
    
    def GetXPosition(self):
        return self.__XPosition
    
    def GetYPosition(self):
        return self.__YPosition
    
    def SetYPosition(self,PYPostion:int):
        if PYPostion>10000:
            PYPostion=10000
        
        if PYPostion<0:
            PYPostion=0

        self.__YPosition=PYPostion
    
    def SetXPosition(self,PXPosition:int):
        if PXPostion>10000:
            PXPostion=10000
        
        if PXPostion<0:
            PXPostion=0
        self.__XPosition=PXPosition

    def Move(self,PDirection:str):
        if PDirection=="up":
            self.__YPosition+=10
        if PDirection=="down":
            self.__YPosition-=10
        if PDirection=="right":
            self.__XPosition+=10
        if PDirection=="left":
            self.__XPosition-=10

class BikeCharacter(Character):
    def __init__(self,PName:str,PXPosition:int,PYPosition:int):
        super().__init__(PName, PXPosition, PYPosition)
   
    def Move(self,PDirection:str):
        if PDirection=="up":
            super().__YPosition+=20
        if PDirection=="down":
            super().__YPosition-=20
        if PDirection=="right":
            super().__XPosition+=20
        if PDirection=="left":
            super().__XPosition-=20
#MAIN
Jack=Character("Jack",50,50)
Karla=BikeCharacter("Karla",100,50)

CharacterToMove=input("which character to move?")
while not(CharacterToMove=="jack" or CharacterToMove=="karla"):
    CharacterToMove=input("no such character \nwhich character to move?")

DirectionToMove=input("which direction to move?")
while not(DirectionToMove=="right" or DirectionToMove=="left" or DirectionToMove=="up" or DirectionToMove=="down"):
    DirectionToMove=input("no such character \nwhich character to move?")

if CharacterToMove=="jack":
    Jack.Move(DirectionToMove)
    print(CharacterToMove,"'s new position is X=",Jack.GetXPosition(),"Y=",Jack.GetYPosition())
elif CharacterToMove=="karla":
    Karla.Move(DirectionToMove)
    print(CharacterToMove,"'s new position is X=",Karla.GetXPosition(),"Y=",Karla.GetYPosition())