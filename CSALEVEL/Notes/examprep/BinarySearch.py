Array=[1,3,5,7,10,35,40,67,89]
def BinarySearch(Array:list,data:int):
    top=len(Array)
    bottom=0
    mid=(top+bottom)//2
    while top>bottom:
        if Array[mid]>data:
            top=mid-1
        elif Array[mid]<data:
            bottom=mid+1
        else:
            return mid
        mid=(top+bottom)//2
    return -1
print(BinarySearch(Array,1))
