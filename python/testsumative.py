

Number=int(input("input"))
currentfactorial=1
count=0
while currentfactorial<Number:
    count=count+1
    currentfactorial=currentfactorial*count

if Number==currentfactorial:
    print(count)
else:
    print("-1")