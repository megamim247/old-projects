def IterativeVowels(Value:str): #returns INTEGER
    #DECLARE Total, LengthString : INTEGER
    #DECLARE FirstCharacter : CHAR
    Total=0
    LengthString=len(Value)
    for X in range(0,LengthString):
        FirstCharacter=Value[0]
        if FirstCharacter=='a' or FirstCharacter=='e' or FirstCharacter=='i' or FirstCharacter=='o' or FirstCharacter=='u':
            Total+=1
        Value=Value[1:len(Value)]
    return Total



def RecursiveVowels(Value:str):
    if len(Value)==0:
        return 0
    else:
        if Value[0]=='a' or Value[0]=='e' or Value[0]=='i' or Value[0]=='o' or Value[0]=='u':
            return RecursiveVowels(Value[1:len(Value)]) +1
        else:
            return RecursiveVowels(Value[1:len(Value)])


#MAIN
#MAIN a(i)
print(IterativeVowels("house"))

#MAIN b(ii)
print(RecursiveVowels("imagine"))