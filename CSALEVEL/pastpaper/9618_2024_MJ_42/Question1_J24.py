def ReadWords(FileName:str):
    global WordArray
    global NumberWords
    try:
        file=open(FileName,"r")
        for n in file:
            WordArray.append(n.strip())
            NumberWords+=1

    except IOError:
        print("file not real")

    Play()
    
def Play():
    print("main word:",WordArray[0])


    NumCorrectAnswers=0
    UserInput=str(input("enter guess:"))
    correct=False
    while UserInput!="no":
        correct=False
        for n in range(0,NumberWords):
            if WordArray[n]==UserInput:
                correct=True
                NumCorrectAnswers+=1
                WordArray[n]=""
        if correct==False:
            print("incorrect answer")
        else:
            print("correct answer")
        UserInput=str(input("enter guess:"))
    print((NumCorrectAnswers*100)/NumberWords)
    for n in range(0,NumberWords):
        if WordArray[n]!="":
            print(WordArray[n])


#MAIN
#DECLARE WordArray : LIST GLOBAL
global WordArray
WordArray=[]
#DECLARE NumberWords : INTEGER GLOBAL
global NumberWords
NumberWords=0
#DECLARE Difficulty : STRING
Difficulty=str(input("what difficulty would you like: easy, medium or hard"))

Difficulty=Difficulty[0].upper() + Difficulty[1:len(Difficulty)]
Difficulty=Difficulty+".txt"

ReadWords(Difficulty)
print(WordArray)
