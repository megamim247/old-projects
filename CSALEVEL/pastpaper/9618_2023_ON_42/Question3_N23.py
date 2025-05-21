import datetime
class Character:
    def __init__(self,PCharacterName:str,PDateOfBirth:datetime.date,PIntelligence:float,PSpeed:int):
        #DECLARE CharacterName : STRING PRIVATE
        #DECLARE DateOfBirth : DATE PRIVATE
        #DECLARE Intelligence : REAL PRIVATE
        #DECLARE Speed : INTEGER PRIVATE
        self.__CharacterName=PCharacterName
        self.__DateOfBirth=PDateOfBirth
        self.__Intelligence=PIntelligence
        self.__Speed=PSpeed

    def SetIntelligence(self,PIntelligence:float):
        self.__Intelligence=PIntelligence
    
    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName
    
    def Learn(self):
        self.__Intelligence*=1.1

    def ReturnAge(self):
        return 2023-self.__DateOfBirth.year

class MagicCharacter(Character):
    def __init__(self,PCharacterName:str,PDateOfBirth:datetime.date,PIntelligence:float,PSpeed:int,PElement:str):
        #DECLARE Element : STRING PRIVATE
        super().__init__(PCharacterName, PDateOfBirth, PIntelligence, PSpeed)
        self.__Element=PElement

    def Learn(self):
        if self.__Element=="water"or self.__Element=="fire":
            super().SetIntelligence(super().GetIntelligence()*1.2)
        elif self.__Element=="earth":
            super().SetIntelligence(super().GetIntelligence()*1.3)
        else:
            super().SetIntelligence(super().GetIntelligence()*1.1)

#MAIN
FirstCharacter=Character("Royal",datetime.date(2019,1,1),70,30)
FirstCharacter.Learn()
print(FirstCharacter.GetName(),"has age",FirstCharacter.ReturnAge(),"Intelligence",FirstCharacter.GetIntelligence())
FirstMagic=MagicCharacter("Light",datetime.date(2018,3,3),75,22,"fire")
FirstMagic.Learn()
print(FirstMagic.GetName(),"has age",FirstMagic.ReturnAge(),"Intelligence",FirstMagic.GetIntelligence())
