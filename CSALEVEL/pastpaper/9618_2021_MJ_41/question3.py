class TreasureChest:
    def __init__(self,Pquestion:str,Panswer:int,Ppoints:int):
        #DECLARE question : STRING PRIVATE
        #DECLARE answer,point : INTEGER PRIVATE
        self.__question=Pquestion
        self.__answer=Panswer
        self.__points=Ppoints
    
    def checkAnswer(self,UserAnswer:int):
        if UserAnswer==self.__answer:
            return True
        else:
            return False
        

    def getQuestion(self):
        return self.__question
    
    def getPoints(self,attempts:int):
        if attempts==1:
            return self.__points
        elif attempts==2:
            return self.__points//2
        elif attempts==3 or attempts==4:
            return self.__points//4
        elif attempts>4:
            return 0

def readData():
    global arrayTreasure
    #DECLARE arrayTreasure : Array(0,4) of TreasureChest
    #DECLARE count,answer : INTEGER
    #DECLARE question : STRING
    
    try:
        file=open("TreasureChestData.txt")
        question=file.readline().strip()
        while question!="":
            answer=file.readline().strip()
            points=file.readline().strip()
            arrayTreasure=TreasureChest(question,int(answer),int(points))
            question=file.readline().strip()
    except IOError:
        print("not a real file")

#MAIN
readData()
#DECLARE userSelection,answerInput,attempts : INTEGER
userSelection=int(input("enter a question number between 1 and 5"))
print(arrayTreasure[userSelection-1].getQuestion())
answerInput=int(input("enter your answer:"))
attempts=1
while not(arrayTreasure[userSelection].checkAnswer(answerInput)):
    answerInput=int(input("Wrong\nenter your answer:"))
    attempts+=1
print("you were awarded: ",arrayTreasure[userSelection].getPoints()," points")