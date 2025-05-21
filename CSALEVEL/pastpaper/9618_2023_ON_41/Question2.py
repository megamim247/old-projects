#DECLARE Queue : ARRAY(0,50) of STRING
#DECLARE HeadPointer,TailPointer : INTEGER
Queue=["" for n in range(0,50)]
HeadPointer=-1
TailPointer=0

def Enqueue(Item:str):
    global Queue,TailPointer
    if TailPointer==50:
        print("Queue full")
    else:
        Queue[TailPointer]=Item
        TailPointer+=1

def Dequeue():
    global Queue,HeadPointer,TailPointer
    if HeadPointer==TailPointer:
        print("Queue empty")
    else:
        HeadPointer+=1
        return Queue[HeadPointer]


def ReadData():
    try:
        file=open("QueueData.txt","r")
        for n in file:
            Enqueue(n.strip())
    except IOError:
        print("file not real")

class RecordData:
    def __init__(self,PID:str,PTotal:int):
        #DECLARE ID : STRING
        #DECLARE Total : INTEGER
        self.ID=PID
        self.Total=PTotal

#DECLARE Records : ARRAY(0,50) of RecordData
Records=[RecordData("",0) for n in range(0,50)]
NumberRecords=0

def TotalData():
    #DECLARE DataAccessed : STRING
    #DECLARE Flay : BOOLEAN
    global NumberRecords,Records
    DataAccessed=Dequeue()
    Flag=False 
    if NumberRecords==0:
        Records[NumberRecords].ID=DataAccessed
        Records[NumberRecords].Total=1
        Flag=True
        NumberRecords+=1
    else:
        for X in range(0,NumberRecords-1):
            if Records[X].ID==DataAccessed:
                Records[X].Total=Records[X].Total+1
                Flag=True
    if Flag==False:
        Records[NumberRecords].ID=DataAccessed
        Records[NumberRecords].Total=1
        NumberRecords+=1
    

def OutputRecords():
    global NumberRecords
    for n in range(0,NumberRecords):
        print("ID ",Records[n].ID," Total ",Records[n].Total)

#MAIN
ReadData()
print(Queue)
for n in range(HeadPointer,TailPointer):
    TotalData()
OutputRecords()
