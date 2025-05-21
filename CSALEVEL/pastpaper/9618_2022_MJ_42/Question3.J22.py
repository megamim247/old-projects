class Card:
    def __init__(self,PNumber:int,PColour:str):
        #DECLARE Number : INTEGER PRIVATE
        #DECLARE Colour : STRING PRIVATE
        self.__Number=PNumber
        self.__Colour=PColour
    
    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour

#MAIN

    
