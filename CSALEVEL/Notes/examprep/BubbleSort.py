Array=[9,4,7,6,1,5,3,2,8,10]

def BubbleSort(Array):
    Swap=True
    length=10
    while Swap:
        Swap=False
        for n in range(0,length-1):
            if Array[n]>Array[n+1]:
                Swap=True
                Array[n],Array[n+1]=Array[n+1],Array[n]
        length-=1
    return Array
print(BubbleSort(Array))

