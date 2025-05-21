#DECLARE ReadFile : PROCEDURE
def ReadFile():
    global DataArray
    try:
        #DECLARE Count : INTEGER
        #DECLARE Line : STRING
        file=open("IntegerData.txt")
        Count=0
        for Line in file:
            DataArray[Count]=int(Line.strip())
            Count+=1
    except IOError:
        print("file not real")

#DECLARE FindValues : FUNCTION
def FindValues():
    global DataArray
    #DECLARE SearchValue,index,count : INTEGER
    SearchValue=0
    while SearchValue>100 or SearchValue<1:
        SearchValue=int(input("enter value to search (whole number between 1 and 100)"))
    count=0
    for index in range(0,100):
        if DataArray[index]==SearchValue:
            count+=1
    return count

def BubbleSort():
    global DataArray

#MAIN
global DataArray
#DECALRE DataArray : ARRAY(0,99) of INTEGER
DataArray=[0 for n in range(0,100)]
ReadFile()
print("the value occurs",FindValues(),"number of times")


