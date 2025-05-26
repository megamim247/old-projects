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

class Hand:
    def __init__(self,PCard1:Card,PCard2:Card,PCard3:Card,PCard4:Card,PCard5:Card):
        #DECLARE Cards : Array[0:9] PRIVATE
        #DECLARE FirstCard,NumberCards : INTEGER PRIVATE
        self.__Cards=[Card(0,"") for n in range(0,10)]
        self.__Cards[0]=PCard1
        self.__Cards[1]=PCard2
        self.__Cards[2]=PCard3
        self.__Cards[3]=PCard4
        self.__Cards[4]=PCard5
        self.__FirstCard=0
        self.__NumberCards=5
    
    def GetCard(self,index:int):
        return self.__Cards[index]

def CalculateValue(hand:Hand):
    #DECLARE count : INTEGER
    #DECLARE card : Card
    count=0
    for n in range(0,5):
        card=hand.GetCard(n)
        if card.GetColour() == "red":
            count+=5
        elif card.GetColour() == "blue":
            count+=10
        elif card.GetColour() == "yellow":
            count+=15
    
    return count
        

#MAIN
#DECLARE Card1,Card2,Card3,Card4,Card5,Card6,Card7,Card8,Card9,Card10,Card11,Card12,Card13,Card14,Card15 : Card
Card1=Card(1,"red")
Card2=Card(2,"red")
Card3=Card(3,"red")
Card4=Card(4,"red")
Card5=Card(5,"red")
Card6=Card(1,"blue")
Card7=Card(2,"blue")
Card8=Card(3,"blue")
Card9=Card(4,"blue")
Card10=Card(5,"blue")
Card11=Card(1,"yellow")
Card12=Card(2,"yellow")
Card13=Card(3,"yellow")
Card14=Card(4,"yellow")
Card15=Card(5,"yellow")

#DECLARE Player1,Player2 : Hand
Player1=Hand(Card(1,"red"),Card(2,"red"),Card(3,"red"),Card(4,"red"),Card(1,"yellow"))
Player2=Hand(Card(2,"yellow"),Card(3,"yellow"),Card(4,"yellow"),Card(4,"yellow"),Card(1,"blue"))

#DECLARE Player1Score,Player2Score : INTEGER
Player1Score=CalculateValue(Player1)
Player2Score=CalculateValue(Player2)

if Player1Score>Player2Score:
    print("Player 1 wins")
if Player1Score<Player2Score:
    print("Player 2 wins")
else:
    print("draw")
