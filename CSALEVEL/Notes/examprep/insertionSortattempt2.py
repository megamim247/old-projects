Array=[9,4,7,6,1,5,3,2,8,10]
print(Array)

for n in range(1,10):
    key=Array[n]
    index=n-1
    while Array[index]>key and index>=0:
        Array[index+1]=Array[index]
        index-=1
    Array[index+1]=key
    print(Array)

print(Array)