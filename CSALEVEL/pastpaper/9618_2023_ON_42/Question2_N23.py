#DECLARE IterativeCalculate : FUNCTION returns INTEGER
def IterativeCalculate(Number:int):
    #DECLARE Total,ToFind : INTEGER
    ToFind=Number
    Total=0
    while Number!=0:
        if ToFind%Number==0:
            Total+=1
        Number-=1
    return Total

#DECLARE RecursiveValue : FUNCTION returns INTEGER
def RecursiveValue(Number:int,ToFind:int):
    if Number==0:
        return 0
    else:
        if ToFind%Number==0:
            return 1 + RecursiveValue(Number-1,ToFind)
        else:
            return RecursiveValue(Number-1, ToFind)

#MAIN
print(IterativeCalculate(10))
print(RecursiveValue(50,50))