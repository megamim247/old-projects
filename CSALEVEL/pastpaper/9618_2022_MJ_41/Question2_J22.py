class Balloon:
    def __init__(self,PColour,PDefenceItem):
        #DEFINE Health : INTEGER PRIVATE
        #DEFINE Colour,DefenceItem : STRING PRIVATE
        self.__Health=100
        self.__Colour=PColour
        self.__DefenceItem=PDefenceItem
        
    def GetDefenceItem(self):
        return self.__DefenceItem
    
    def ChangeHealth(self,changeHealth):
        self.__Health+=changeHealth
    
    def CheckHealth(self):
        if self.__Health<=0:
            return True
        else:
            return False
    
def Defend(PBalloon:Balloon):
    #DEFINE Strength : INTEGER
    Strength=int(input("Strength of opponent:" ))
    PBalloon.ChangeHealth(-Strength)
    print("Balloon defence Item:",PBalloon.GetDefenceItem())
    if Balloon1.CheckHealth():
        print("No health remaining")
    else:
        print("Health remaining")
    return PBalloon



#MAIN
#DEFINE DefenceItem : STRING
#DEFINE Colour : STRING
DefenceItem=str(input("enter defence item"))
Colour=str(input("enter balloon colour"))
Balloon1=Balloon(Colour,DefenceItem)
Balloon1=Defend(Balloon1)