
#node is a record
class node:
    def __init__(self,Pleft_pointer,Pdata,Pright_pointer):
        self.left_pointer=Pleft_pointer
        self.data=Pdata
        self.right_pointer=Pright_pointer

#initialization

Binarytree=[node(-1,-1,-1) for n in range(0,6)]
FreePointer=0
def add(item:int):
    global FreePointer
    global Binarytree
    if FreePointer!=len(Binarytree):
        CurrentPointer=0
        PreviousPointer=0
        if FreePointer==0:
            Binarytree[0].data=item
            FreePointer=1
        else:
            while CurrentPointer!=-1:
                TurnedRight=False
                PreviousPointer=CurrentPointer
                if item<Binarytree[CurrentPointer].data:
                    TurnedRight=True
                    CurrentPointer=Binarytree[CurrentPointer].right_pointer
                elif item>Binarytree[CurrentPointer].data:
                    TurnedRight=False
                    CurrentPointer=Binarytree[CurrentPointer].left_pointer

            if TurnedRight:
                Binarytree[PreviousPointer].right_pointer=FreePointer
            else:
                Binarytree[PreviousPointer].left_pointer=FreePointer
    
            Binarytree[FreePointer].data=item
            FreePointer+=1
                

        
    else:
        print("full")
                
    


def search(item:int):

    pass

add(5)

add(6)
add(4)
add(9)
add(8)
add(10)
add(1)
add(2)
add(3)
print("###########")
for n in Binarytree:
    print(n.right_pointer,n.data,n.left_pointer)