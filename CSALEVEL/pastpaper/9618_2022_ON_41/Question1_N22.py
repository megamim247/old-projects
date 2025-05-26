def ReadFile():
    #DECLARE ReadData : STRING
    #DECLARE count : INTEGER
    global DataArray
    try:
        file=open("IntegerData.txt","r")
        ReadData=file.readline().strip()

        count=0
        while ReadData!="":
            DataArray[count]=int(ReadData)
            ReadData=file.readline().strip()
            count+=1
        file.close()
    except IOError:
        print("file is not real")

def FindValues():
    #DECLARE SearchValue : INTEGER
    #DECLARE count : INTEGER
    count=0
    global DataArray
    SearchValue=int(input("enter search value:"))
    while SearchValue>100 or SearchValue<0:
        SearchValue=int(input("enter search value:"))
    for n in DataArray:
        if n==SearchValue:
            count+=1
    return count

def BubbleSort():
    #DECLARE Swap : BOOLEAN
    #DECLARE temp : integer
    global DataArray
    swap="True"
    length=len(DataArray)
    while swap:
        for n in range(0,length):
            if DataArray[n]>DataArray[n+1]:
                temp=DataArray[n]
                DataArray[n]=DataArray[n+1]
                DataArray[n+1]=temp
        length-=1

    for n in DataArray:
        print(n,end=",")

#MAIN
#DECLARE DataArray : Array[1:100] of INTEGER GLOBAL
global DataArray
DataArray=[0 for n in range(0,100)]

ReadFile()
print("the value occurs ",FindValues()," times")


