#DECLARE PrintArray : PROCEDURE
def PrintArray(Array:list):
    for n in Array:
        print(n, end=" ")

#DECLARE LinearSearch : FUNCTION returns 
def LinearSearch(Array:list,SearchVal:int):
    #DECLARE count : INTEGER
    count=0
    for n in Array:
        if n==SearchVal:
            count+=1
    return count

#MAIN
#DECLARE DataArray : ARRAY(0,25) OF ITNTEGER
DataArray=[0 for n in range(0,25)]
try:
    #DECLARE count : INTEGER
    count=0
    file=open("Data.txt","r")
    for n in file:
        DataArray[count]=int(n.strip())
        count+=1
    file.close()
except IOError:
    print("file is not real")

PrintArray(DataArray)

#InputVal : INTEGER
InputVal=int(input("\nenter a numhber between 0 and 100 inclusive"))
while InputVal<0 or InputVal>100:
    InputVal=int(input("no, enter a value between 0 and 100"))

print("The number ",InputVal,"is found ",LinearSearch(DataArray,InputVal)," time")
