def ReadHighScores():
    global Players,Scores
    try:
        file=open("HighScore.txt")
        Line=file.readline().strip()
        count=0
        while len(Line)>0:
            Players[count]=Line[:3]
            Line=int(file.readline().strip())
            Scores[count]=Line
            Line=file.readline().strip()
            count+=1

        file.close()
    except IOError:
        print("file is not real")

def OutputHighScores():
    global Players,Scores
    for n in range(0,len(Players)):
        print(Players[n]," ",Scores[n])

def addtotopten(Player,Score):
    global Players,Scores
    count=0
    while count<=10:
        if Score>Scores[count]:
            for n in range(len(Players)-1,count,-1):
                Scores[n]=Scores[n-1]
                Players[n]=Players[n-1]
            Scores[count]=Score
            Players[count]=Player
            count=10
        count+=1
            
#MAIN
#DECLARE Players : ARRAY(0,11) of STRING GLOBAL
#DECLARE Scores : ARRAY(0,11) of INTEGER GLOBAL
global Players,Scores
Players=["" for n in range(0,11)]
Scores=[0 for n in range(0,11)]

def WriteTopTen():
    try:
        file=open("NewTopTen","w")
        for n in range(0,10):
            file.write(Players[n])
            file.write(Scores[n])
        file.close()
    except:
        print("file is not real")
ReadHighScores()
OutputHighScores()
#DECLARE inputname : STRING
#DECLARE inputscore : INTEGER
inputname=str(input("enter player name"))
while len(inputname)!=3:
    inputname=str(input("enter player name "))
inputscore=int(input("enter score 1 to 100000 "))
while inputscore>100000 or inputscore<1:
    inputscore=str(input("enter score 1 to 100000 "))
addtotopten(inputname,inputscore)
OutputHighScores()