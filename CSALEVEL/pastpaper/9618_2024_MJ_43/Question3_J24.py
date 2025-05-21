#DECLARE Enqueue : FUNCTION returns BOOLEAN
def Enqueue(data:str):
    global QueueHead,QueueData,QueueTail
    if QueueTail!=QueueHead-1:
        if QueueTail==19:
            QueueTail=-1
        QueueTail+=1
        QueueData[QueueTail]=data
        return True
    else:
        return False

#DECLARE Dequeue : FUNCTION returns STRING
def Dequeue():
    global QueueHead,QueueData,QueueTail
    if QueueTail!=QueueHead:
        if QueueHead==20:
            QueueHead=-1
        QueueHead+=1
        data=QueueData[QueueHead]
        return data
    else:
        return "false"

#DECLARE StoreItems : PROCEDURE
def StoreItems():
    #DECLARE data : STRING
    #DECLARE invalidcount : INTEGER
    invalidcount=0
    for n in range(0,10):
        data=str(input("enter data"))
        if data[6]!="X":
            if len(data)==7 and ((int(data[0])+int(data[2])+int(data[4])+3*(int(data[1])+int(data[3])+int(data[5])))//10==int(data[6])):
                inserted=Enqueue(data[0:5])
                if inserted:
                    print("item valid and inserted")
                else:
                    print("queue full")
            else:
                invalidcount+=1
        else:
            if len(data)==7 and ((int(data[0])+int(data[2])+int(data[4])+3*(int(data[1])+int(data[3])+int(data[5])))//10==10):
                inserted=Enqueue(data[0:6])
                if inserted:
                    print("item valid and inserted")
                else:
                    print("queue full")
            else:
                invalidcount+=1
    print("Number of invalid items:",invalidcount)

#MAIN
#DECLARE QueueData : ARRAY(0,20) of STRING
global QueueData
QueueData=["" for n in range(0,20)]
#DECLARE QueueHead,QueueTail : INTEGER
global QueueHead
global QueueTail
QueueHead=-1
QueueTail=-1
StoreItems()
#DECLARE value : STRING
value=Dequeue()
if value !="false":
    print("data: ",value)
else:
    print("queue empty")
