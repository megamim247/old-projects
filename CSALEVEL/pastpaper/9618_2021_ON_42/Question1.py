#DECLARE Unknown : FUNCION returns INTEGER
def Unknown(X:int,Y:int):
    if X<Y:
        print(X+Y)
        return Unknown(X+1,Y)*2
    else:
        if X==Y:
            return 1
        else:
            print(X+Y)
            return Unknown(X-1,Y)//2

def IterativeUnknown(X:int,Y:int):
    #DECLARE ReturnValue : INTEGER
    ReturnValue=1
    while X!=1:
        if X<Y:
            print(X+Y)
            X+=1
            ReturnValue*=2
        else:
            if X==Y:
                return ReturnValue
            else:
                print(X+Y)
                X-=1
                ReturnValue//=2
                
        

#MAIN
print("parameters called: 10,15")
print(Unknown(10,15))
print("parameters called: 10,10")
print(Unknown(10,10))
print("parameters called: 15,10")
print(Unknown(15,10))

print("\nIterative")
print("parameters called: 10,15")
print(IterativeUnknown(10,15))
print("parameters called: 10,10")
print(IterativeUnknown(10,10))
print("parameters called: 15,10")
print(IterativeUnknown(15,10))