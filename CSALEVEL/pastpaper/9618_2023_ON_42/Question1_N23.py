#DECLARE PushData : PROCEDURE
def PushData(param:str):
    global StackConsonant,StackVowel,ConsonantTop,VowelTop
    if param in ["a","e","i","o","u"]:
        if VowelTop<100:
            StackVowel[VowelTop]=param
            VowelTop+=1
        else:
            print("Vowel Stack full")
    else:
        if ConsonantTop<100:
            StackConsonant[ConsonantTop]=param
            ConsonantTop+=1
        else:
            print("Consonant Stack full")

#DECLARE ReadData : PROCECDURE
def ReadData():
    try:
        file=open("StackData.txt")
        for n in file:
            PushData(n.strip())
        file.close()
    except IOError:
        print("file not real")

#DECLARE PopVowel : FUNCTION returns STRING
def PopVowel():
    global VowelTop,StackVowel
    if VowelTop<100:
        VowelTop-=1
        return StackVowel[VowelTop]

#DECLARE PopConsonant : FUNCTION returns STRING
def PopConsonant():
    global ConsonantTop,StackConsonant
    if ConsonantTop<100:
        ConsonantTop-=1
        return StackConsonant[ConsonantTop]


#MAIN
global StackVowel
global StackConsonant
#DECLARE StackVowel : ARRAY(0,100) of STRING GLOBAL
#DECLARE StackConstant : ARRAY(0,100) of STRING GLOBAL
StackVowel=["" for n in range(0,100)]
StackConsonant=["" for n in range(0,100)]
global VowelTop, ConsonantTop
#DECLARE VowelTop, ConsonantTop : INTEGER GLOBAL
VowelTop=0
ConsonantTop=0
ReadData()
#DECLARE userChoice : STRING
for n in range(0,5):
    userChoice=str(input("enter your choice(vowel or consonant)"))
    if userChoice=="vowel":
        print(PopVowel())
    else:
        print(PopConsonant())