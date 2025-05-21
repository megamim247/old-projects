#DEFINE StackOutput : PROCEDURE
def StackOutput():
    global StackData,StackPointer
    for n in StackData:
        print(n)
    print(StackPointer)

#DEFINE Push : FUNCTION returns BOOLEAN
def Push(data:int):
    global StackPointer,StackData
    if StackPointer==10:
        return False
    else:
        StackData[StackPointer]=data
        StackPointer+=1
        return True

#DEFINE Pop : FUNCTION returns INTEGER
def Pop():
    global StackPointer,StackData
    if StackPointer==0:
        return -1
    else:
        StackPointer-=1
        return StackData[StackPointer]
    


#MAIN
#DECLARE StackData : Array(0,9) of INTEGER
global StackData
StackData=[0 for n in range(0,10)]
#DECLARE StackPointer : INTEGER
global StackPointer
StackPointer=0
#DECLARE Number : INTEGER
#DECLARE Pushed : BOOLEAN
for n in range(0,11):
    if Push(int(input("enter number to be pushed onto stack"))):
        print("Pushed successfully")
    else:
        print("list full")
StackOutput()
#DECLARE popped : BOOLEAN
Pop()
Pop()
StackOutput()