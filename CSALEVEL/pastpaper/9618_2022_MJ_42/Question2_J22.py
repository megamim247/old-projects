import random
#DECLARE ArrayOutPut : PROCEDURE
def ArrayOutPut():
    #DECLARE ArrayLength=10
    global ArrayData
    ArrayLength=10
    for Row in range(0,ArrayLength):
        for Column in range(0,ArrayLength):
            print(ArrayData[Row][Column],end=" ")
        print("")

#DECLARE BinarySearch : FUNCTION returns INTEGER
def BinarySearch(SearchArray:list,Lower:int,Upper:int,SearchValue:int):
    if Upper >= Lower:
        Mid=Lower+(Upper-1)//2
        if SearchArray[0][Mid]==SearchValue:
            return Mid
        else:
            if SearchArray[0,Mid]>SearchValue:
                return BinarySearch(SearchArray,Mid+1,Upper,SearchValue)
            else:
                return BinarySearch(SearchArray,Lower,Mid-1,SearchValue)
    return -1







#MAIN
#DECLARE ArrayData : Array(0,9)(0,10) of INTEGER GLOBAL
global ArrayData
ArrayData=[[random.randint(1,100) for n in range(0,10)] for n2 in range(0,10)]

#DECLARE ArrayLength,TempValue : INTEGER
ArrayLength=10
for X in range(0,ArrayLength):
    for Y in range(0,ArrayLength-1):
        for Z in range(0,ArrayLength-Y-1):
            if ArrayData[X][Z]>ArrayData[X][Z+1]:
                TempValue=ArrayData[X][Z]
                ArrayData[X][Z]=ArrayData[X][Z+1]
                ArrayData[X][Z+1]=TempValue

ArrayOutPut()
print(BinarySearch(ArrayData[0],0,10,ArrayData[9]))
print(BinarySearch(ArrayData[0],0,10,990))





