class SaleData:
    def __init__(self,PID:str,PQuantity:int):
        self.ID=PID
        self.Quantity=PQuantity

#DEFINE CircularQueue : Array(0,5) of SaleData
#DEFINE Head,Tail,NumberOfItems :INTEGER
Head=0
Tail=0
NumberOfItems=0
CircularQueue=[SaleData(-1,"") for n in range(0,5)]

def Enqueue(record:SaleData):
    global NumberOfItems,CircularQueue,Tail
    if NumberOfItems==5:
        return -1
    else:
        if Tail==4:
            Tail=0 
        else:
            Tail+=1
        CircularQueue[Tail]=record
        NumberOfItems+=1
        return 1

def Dequeue():
    global NumberOfItems,Head,CircularQueue
    #DEFINE record : SaleData
    record=SaleData(0,"")
    if NumberOfItems==0:
        return record
    else:
        if Head==4:
            Head=0
        else:
            Head+=1
        record=CircularQueue[Head]
        NumberOfItems-=1
        return record

def EnterRecord(ID:str,Quantity:int):
    #DEFINE record : SaleData
    record=SaleData(ID,Quantity)
    entered=Enqueue(record)
    if entered==-1:
        print("Full")
    else:
        print("stored")

#MAIN
EnterRecord("ADF",10)
EnterRecord("OOP",1)
EnterRecord("BXW",5)
EnterRecord("XXZ",22)
EnterRecord("HQR",6)
EnterRecord("LLP",3)
Dequeue()
EnterRecord("LLP",3)
for n in CircularQueue:
    print("ID: ",n.ID," Quantity: ",n.Quantity)