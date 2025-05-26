Array=[9,4,7,6,1,5,3,2,8,10]

def InsertionSort(Array):
    for n in range(1,10):
        key=Array[n]
        index=n
        while key<Array[index-1] and index>0:
            Array[index]=Array[index-1]
            index-=1
            print("swap")
        Array[index]=key
        print(Array)
    return Array

print(InsertionSort(Array))