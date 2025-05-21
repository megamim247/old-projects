#DEFINE Animals : Array(0,10) of STRING
Animals=["" for n in range(0,10)]
Animals=["horse","lion","rabbit","mouse","bird","deer","whale","elephant","kangaroo","tiger"]

def SortDescending():
    global Animals
    #DECLARE ArrayLength : INTEGER
    #DECLARE Temp : STRING
    ArrayLength=len(Animals)
    for x in range(0,ArrayLength-1):
        for y in range(0, ArrayLength -x -1):
            if Animals[y][0]<Animals[y+1][0]:
                Temp=Animals[y]
                Animals[y]=Animals[y+1]
                Animals[y+1]=Temp

#MAIN
SortDescending()
for n in range(0,len(Animals)):
    print(Animals[n])