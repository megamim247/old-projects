#PROCEDURE Initialise
def Initialise():
    global DataStored
    global NumberItems
    NumberItems=0
    NumberItems=int(input("how many items whould you like to store?"))
    while NumberItems>20 or NumberItems<1:
        NumberItems=int(input("Invalid number of items, please try again"))
    for n in range(NumberItems):
        DataStored[n]=int(input("Number to store:"))

#PROCEDURE BubbleSort
def BubbleSort():
    global DataStored
    global NumberItems
    #DECLARE temp,count : INTEGER
    #DECLARE swap : BOOLEAN
    passes=1
    swap=True
    while swap:
        swap=False
        for n in range(0,NumberItems-passes):
            if DataStored[n]>DataStored[n+1]:
                temp=DataStored[n]
                DataStored[n]=DataStored[n+1]
                DataStored[n+1]=temp
                swap=True
        passes+=1

def BinarySearch(DataToFind:int):
    global DataStored
    global NumberItems
    ub=NumberItems
    lb=0
    found=False
    while lb<ub:
        mid=(ub+lb)//2
        if DataStored[mid]<DataToFind:
            lb=mid
            found=True
        elif DataStored[mid]>DataToFind:
            ub=mid
            found=True
        else:
            return mid
        
    return -1


#MAIN
#DECLARE DataStored : ARRAY(0,20) of INTEGER
global DataStored
DataStored=[0 for n in range(0,20)]
#DECLARE NumberItems : INTEGER
global NumberItems

NumberItems=0
Initialise()

BubbleSort()
for n in range(0,NumberItems):
    print(DataStored[n])

DataToFind=int(input("data to find"))
print("index:",BinarySearch(DataToFind))