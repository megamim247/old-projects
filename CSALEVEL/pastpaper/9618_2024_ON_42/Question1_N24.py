class EventItem:
    def __init__(self,PEventName:str,PType:str,PDifficulty:int):
        #DECLARE EventName,Type : STRING PRIVATE
        #DECLARE Difficulty : INTEGER PRIVATE
        self.__EventName=PEventName
        self.__Type=PType
        self.__Difficulty=PDifficulty
    
    def GetName(self):
        return self.__EventName
    
    def GetDifficulty(self):
        return self.__Difficulty

    def GetEventType(self):
        return self.__Type

class Character:
    def __init__(self,PCharacterName:str,PJump:int,PSwim:int,PRun:int,PDrive:int):
        #DECLARE CharacterName : STRING PRIVATE
        #DECLARE Jump,Swim,Run,Drive : INTEGER PRIVATE
        self.__CharacterName=PCharacterName
        self.__Jump=PJump
        self.__Swim=PSwim
        self.__Run=PRun
        self.__Drive=PDrive
    
    def GetName(self):
        return self.__CharacterName
    
    def CalculateScore(self,Type:str,Difficulty:int):
        if Type=="jump":
            if self.__Jump>Difficulty:
                return 100
            else:
                return 20*(5-(Difficulty-self.__Jump)) 
        elif Type=="swim":
            if self.__Swim>Difficulty:
                return 100
            else:
                return 20*(5-(Difficulty-self.__Swim))
        elif Type=="run":
            if self.__Run>Difficulty:
                return 100
            else:
                return 20*(5-(Difficulty-self.__Run))
        elif Type=="drive":
            if self.__Drive>Difficulty:
                return 100
            else:
                return 20*(5-(Difficulty-self.__Drive))
        

#MAIN
#DECLARE Group : Array(0,5) of EventItem
Group=[EventItem("","",0) for n in range(0,5)]
Group[0]=EventItem("Bridge","jump",3)
Group[1]=EventItem("Water wade","swim",4)
Group[2]=EventItem("100 mile run","run",5)
Group[3]=EventItem("Gridlock","drive",2)
Group[4]=EventItem("Wall on wall","jump",4)

#DECLARE Tarz,Geni : Character
Tarz=Character("Tarz",5,3,5,1)
Geni=Character("Geni",2,2,3,4)

#DECLARE SumTarz, SumGeni : INTEGER
SumGeni=0
SumTarz=0
for n in Group:
    if Tarz.CalculateScore(n.GetEventType(),n.GetDifficulty())<Geni.CalculateScore(n.GetEventType(),n.GetDifficulty()):
        print("Geni wins")
        SumGeni+=1
    elif Tarz.CalculateScore(n.GetEventType(),n.GetDifficulty())>Geni.CalculateScore(n.GetEventType(),n.GetDifficulty()):
        print("Tarzl wins")
        SumTarz+=1
    else:
        print("draw")

if SumTarz>SumGeni:
    print("Tarz won the most points")
elif SumGeni>SumTarz:
    print("Geni won the most points")
else:
    print("overall draw")

