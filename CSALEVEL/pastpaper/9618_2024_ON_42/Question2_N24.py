class Queue:
    def __init__(self,PQueue:list,PHeadPointer:int,PTailPointer:int):
        #DECLARE QueueArray : ARRAY(0,100) of INTEGER
        #DECLARE HeadPointer,TailPointer : INTEGER
        self.QueueArray=PQueue
        self.HeadPointer=PHeadPointer
        self.TailPointer=PTailPointer

#DECLARE Enqueue : FUNCTION returns INTEGER
def Enqueue(TheData:int):
    global TheQueue #BYREF
    if TheQueue.HeadPointer==-1:
        TheQueue.QueueArray[TheQueue.TailPointer]=TheData
        TheQueue.HeadPointer=0
        TheQueue.TailPointer+=1
        return 1
    else:
        if TheQueue.TailPointer>100:
            return -1
        else:
            TheQueue.QueueArray[TheQueue.TailPointer]=TheData
            TheQueue.TailPointer+=1
            return 1
#DECLARE ReturnAllData : FUNCTION returns STRING
def ReturnAllData():
    global TheQueue
    #DECLARE ReturnString : STRING
    ReturnString=""
    for n in range(TheQueue.HeadPointer,TheQueue.TailPointer):
        ReturnString+=str(TheQueue.QueueArray[n])+" "
    return ReturnString.strip

#MAIN
global TheQueue
TheQueue=Queue([-1 for n in range(0,100)],-1,0)
#DECLARE IntInput : INTEGER
for n in range(0,10):
    IntInput=int(input("enter an integer with value 0 or greater"))
    while IntInput<0 and not(IntInput.isnum):
        IntInput=int(input("enter an integer with value 0 or greater"))

