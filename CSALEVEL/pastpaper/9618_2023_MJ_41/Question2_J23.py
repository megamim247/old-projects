class Vehicle:
    def __init__(self,PID:str,PMaxSpeed:int,PCurrentSpeed:int,PIncreaseAmount:int,PHorizontalPosition:int):
        #DECLARE ID : STRING PRIVATE
        #DECLARE MaxSpeed, CurrentSpeed, IncreaseAmount, HorizontalPosition : INTEGER PRIVATE
        self.__ID=PID
        self.__MaxSpeed=PMaxSpeed
        self.__CurrentSpeed=PCurrentSpeed
        self.__IncreaseAmount=PIncreaseAmount
        self.__HorizontalPosition=PHorizontalPosition

    #DECLARE GetCurrentSpeed : FUNCTION returns INTEGER
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    #DECLARE GetIncreaseAmount : FUNCTION returns INTEGER
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    #DECLARE GetHorizontalPosition : FUNCTION returns INTEGER
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    #DECLARE GetMaxSpeed : FUNCTION returns INTEGER
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    #DECLARE SetCurrentSpeed : PROCEDURE
    def SetCurrentSpeed(self,PCurrentSpeed:int):
        self.__CurrentSpeed=PCurrentSpeed
    
    #DECLARE SetCurrentSpeed : PROCEDURE
    def SetCurrentSpeed(self,PHorizontalPosition:int):
        self.__HorizontalPosition=PHorizontalPosition

    def IncreaseSpeed(self):
        self.__CurrentSpeed+=self.__IncreaseAmount

class Helicopter(Vehicle):
    def __init__(self, PID, PMaxSpeed, PCurrentSpeed, PIncreaseAmount, PHorizontalPosition,P[']']):
        super().__init__(PID, PMaxSpeed, PCurrentSpeed, PIncreaseAmount, PHorizontalPosition)
