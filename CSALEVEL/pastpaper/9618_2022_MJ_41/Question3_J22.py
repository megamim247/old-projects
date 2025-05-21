#DEFINE QueueArray : ARRAY(0,10) of STRING
QueueArray=["" for n in range(0,10)]
HeadPointer=0
TailPointer=0
NumberItems=0
#DEFINE Enqueue : FUNCTION returns BOOLEAN
def Enqueue(DataToAdd:str):
    global HeadPointer, TailPointer,NumberItems,QueueArray
    if NumberItems==10:
        return False
    QueueArray[TailPointer]=DataToAdd
    if TailPointer>=9:
        TailPointer=0
    else:
        TailPointer+=1
    NumberItems+=1
    return True

#DEFINE Dequeue : FUNCTION returns BOOLEAN
def Dequeue():
    global HeadPointer,TailPointer,QueueArray,NumberItems
    if NumberItems==0:
        return False
    if HeadPointer>=9:
        HeadPointer=0
    else:
        HeadPointer+=1
    NumberItems+=1
    return QueueArray[HeadPointer]

#DEFINE INP : STRING
for n in range(0,11):
    INP=str(input("enter: "))
    Enqueue(INP)

print(Dequeue())
print(Dequeue())