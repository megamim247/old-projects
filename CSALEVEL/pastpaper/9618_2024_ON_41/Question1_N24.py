#DECLARE ReadData : FUNCTION returns ARRAY(0,45) of STRING
def ReadData():
    #DECLARE Array : ARRAY(0,45) of STRING 
    Array=["" for n in range(0,45)]
    #DECLARE count : INTEGER
    count=0 
    try:
        file=open("Data.txt","r")
        for n in file:
            Array[count]=n.strip()
            count+=1
        file.close()
        return Array
    except IOError:
        print("file is not real")

#DECLARE FormatArray : FUNCTION returns STRING
def FormatArray(Array:list):
    #DECLARE String : STRING
    String=""
    for n in Array:
        String+=n+" "
    return String

#DECLARE CompareStrings : FUNCTION returns INTEGER
def CompareStrings(String1:str,String2:str):
    #DECLARE count1,count2 : INTEGER
    index1=0
    index2=0
    for n in range(len(String1)):
        charmap="abcdefghijklmnopqrstuvwxyz"
        for n1 in range(0,26):
            if charmap[n1]==String1[n]:
                index1=n1
        for n2 in range(0,26):
            if charmap[n2]==String2[n]:
                index2=n2
        if index1>index2:
            return 2
        elif index1<index2:
            return 1

#DECLARE Bubble : FUNCTION returns ARRAY(0,45) of STRING
def Bubble(Array:list):
    #DECLARE Swap : BOOLEAN
    #DECLARE passes : INTEGER
    #DECLARE temp : STRING
    passes=0
    swap=True
    while swap:
        passes+=1
        swap=False
        for n in range(0,45-passes):
            if CompareStrings(Array[n],Array[n+1])==2:
                temp=Array[n]
                Array[n]=Array[n+1]
                Array[n+1]=temp
                swap=True
    return Array

#MAIN
#DECLARE Array : ARRAY(0,45) of STRING
Array=["" for n in range(0,45)]
Array=ReadData()
Array=Bubble(Array)
print(FormatArray(Array))

