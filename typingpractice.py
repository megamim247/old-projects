from random import randint

charectars=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"\
           ,"r","s","t","u","v","w","x","y","z"]
wrong=[]
right=[]
data=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while True:
    n=randint(0,25)
    x=0
    while not n in wrong and x<2:
        x+=1
        n=randint(0,25)
    i=input(charectars[n])
    if i == charectars[n]:
        try:
            wrong.remove(n)
        except:
            pass
        try:
            right.append(n)
        except:
            pass
        print("yes")
    else:
        try:
            wrong.append(n)
        except:
            pass
        try:
            right.remove(n)
        except:
            pass
        print("no")
