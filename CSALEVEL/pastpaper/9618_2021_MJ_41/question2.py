#DEFINE linearSearch : FUNCTION returns BOOLEAN
def linearSearch(searchValue:int):
    global arrayData
    #DEFINE Found
    Found=False

    for n in range(0,10):
        if arrayData[n]==searchValue:
            Found=True
    return Found

#DEFINE bubbleSort : PROCEDURE
def bubbleSort():
    global arrayData
    #DECLARE temp : INTEGER
    for x in range(0,10):
        for y in range(0,10):
            if arrayData[y]>arrayData[y+1]:
                temp=arrayData[y]
                arrayData[y]=arrayData[y+1]
                arrayData[y+1]=temp


#MAIN
#DEFINE arrayData : ARRAY(0,9) OF INTEGER
#DEFINE userinput : INTEGER
global arrayData
arrayData=[0 for n in range(0,10)]
arrayData=[10,5,6,7,1,12,13,15,21,8]
userinput=int(input("enter search value"))
if linearSearch(userinput):
    print("input is in the array")
else:
    print("not found in array")


