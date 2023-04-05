import random
#datacreate
data=[]
numstr=["0","1","2","3","4","5","6","7","8","9"]
startdeal=11
i=0
#datamaker:
data.append("red:"+str(i))
data.append("blue:"+str(i))
data.append("green:"+str(i))
data.append("yellow:"+str(i))

for i in range(1,10):
    for n in range(2):
        data.append("red:"+str(i))
        data.append("blue:"+str(i))
        data.append("green:"+str(i))
        data.append("yellow:"+str(i))

it=":skip"
for n in range(2):
    data.append("red"+str(it))
    data.append("blue"+str(it))
    data.append("green"+str(it))
    data.append("yellow"+str(it))

it=":draw2"
for n in range(2):
    data.append("red"+str(it))
    data.append("blue"+str(it))
    data.append("green"+str(it))
    data.append("yellow"+str(it))

it=":reverse"
for n in range(2):
    data.append("red"+str(it))
    data.append("blue"+str(it))
    data.append("green"+str(it))
    data.append("yellow"+str(it))

it=" :draw4"
for n in range(4):
    data.append(str(it))

it=" :wild"
for n in range(4):
    data.append(str(it))

def numinlist(element,list):
    count=0
    for n in list:
        if n==element:
            count+=1
    return count

#deck
def createdeck():
    data
    packet=""
    deck=[]
    nub=[]
    for n in range(108):
        nub.append(n)
    for n in data:
        packet=nub[random.randint(0,len(nub)-1)]
        del nub[nub.index(packet)]
        deck.append(data[packet])
    return deck

def createnewdeck(hand1,hand2):
    data
    packet=""
    deck=[]
    nub=[]
    for n in range(108):
        nub.append(n)
    for n in data:
        packet=nub[random.randint(0,len(nub)-1)]
        del nub[nub.index(packet)]
        deck.append(data[packet])
    for n in deck:
        if n in hand1:
            deck.remove(n)
    for n in deck:
        if n in hand2:
            deck.remove(n)
    return deck

#startdeal
def deal(startdeal,deck):
    hand=[]
    for n in range(startdeal):
        hand.append(deck[n])
        del deck[n]
    return hand

def play1(hand,hando,play,deck):
    numstr=["0","1","2","3","4","5","6","7","8","9"]
    skiplist=["wild","draw4","skip","reverse"]
    wilds=["wild","draw4"]
    potind=[]
    handcolours=[]
    handvalues=[]
    play=play.rsplit(":")
    ind=-1
    skip=False
    draw2=False
    draw4=False
    card=""
    #handcolours
    for n in hand:
        handcolours.append(n.rsplit(":")[0])
    #handvalues
    for n in hand:
        handvalues.append(n.rsplit(":")[1])
    #is draw?
    if play[1]=="draw2" and len(deck)>2:
        draw2=True
        for n in range(0,2):
            hand.append(deck[0])
            del deck[0]

    if play[1]=="draw4" and len(deck)>4:
        draw4=True
        for n in range(0,4):
            hand.append(deck[0])
            del deck[0]

    #is skipped?

    if play[1] in skiplist:
        skip=True

    if play[1]=="sr":
        play[1]= "reverse"
    if play[1]=="s":
        play[1]= "skip"
        
    #numbers

    if skip==False:
        for n in hand:
            sp=n.rsplit(":")
            if play[1] in numstr:
                if play[0]==sp[0]:
                    ind=hand.index(n)
                    if ind in potind:
                        potind.remove(ind)
                    potind.append(ind)
                if play[1]==sp[1]:
                    ind=hand.index(n)
                    if ind in potind:
                        potind.remove(ind)
                    potind.append(ind)
            if play[0] in handcolours:
                if play[0]==sp[0]:
                    ind=hand.index(n)
                    if ind in potind:
                        potind.remove(ind)
                    potind.append(ind)
                if play[1]==sp[1]:
                    ind=hand.index(n)
                    if ind in potind:
                        potind.remove(ind)
                    potind.append(ind)
    
    #wild

    if play[0]==" ":
        potind=[]
        for n in range(0,len(hand)):
            potind.append(n)

    if skip==False and ind==-1:
        for n in hand:
            sp=n.rsplit(":")
            if sp[1] in wilds:
                ind=hand.index(n)
                if ind in potind:
                    potind.remove(ind)
                potind.append(ind)

    #draw

    if ind ==-1 and len(deck)>0:
        hand.append(deck[0])
        del deck[0]
        if not(skip):
            for n in hand:
                sp=n.rsplit(":")
                if play[1] in numstr:
                    if play[0]==sp[0]:
                        ind=hand.index(n)
                        if ind in potind:
                            potind.remove(ind)
                        potind.append(ind)
                    if play[1]==sp[1]:
                        ind=hand.index(n)
                        if ind in potind:
                            potind.remove(ind)
                        potind.append(ind)
                if play[0] in hand:
                    if play[0]==sp[0]:
                        ind=hand.index(n)
                        if ind in potind:
                            potind.remove(ind)
                        potind.append(ind)
                    if play[1]==sp[1]:
                        ind=hand.index(n)
                        if ind in potind:
                            potind.remove(ind)
                        potind.append(ind)
    #skip
    
    if play[1]=="s" and ind==-1:
        for n in hand:
            sp=n.rsplit(":")
            if play[0] ==sp[0] and sp[1]in skiplist:
                ind=hand.index(n)
                if ind in potind:
                    potind.remove(ind)
                potind.append(ind)

    #calculation
    print(potind)

    if ind!=-1 and skip!=True:
        ind=potind[random.randint(0,len(potind)-1)]

    for n in potind:
        c=hand[ind]
        c=c.rsplit(":")
        if numinlist(c[0],handcolours)>1 and c in skiplist:
            ind=n
            if (len(hand)<8 or len(hando)<8) and numinlist(c[0],handcolours)>2:
                break
        
        if (c[1]=="draw2" or c[1]=="draw4") and len(hando)<6:
            ind=n
            if len(hando)<5:
                break



    if skip==False and ind!=-1:
        card=hand[ind]
        del hand[ind]
    else:
        skip=True
    return card,hand,deck,skip

def play2(hand,hando,play,deck):
    numstr=["0","1","2","3","4","5","6","7","8","9"]
    skiplist=["wild","draw4","skip","reverse"]
    wilds=["wild","draw4"]
    potind=[]
    handcolours=[]
    handvalues=[]
    play=play.rsplit(":")
    ind=-1
    skip=False
    draw2=False
    draw4=False
    card=""
    #handcolours
    for n in hand:
        handcolours.append(n.rsplit(":")[0])
    #handvalues
    for n in hand:
        handvalues.append(n.rsplit(":")[1])
    #is draw?
    if play[1]=="draw2" and len(deck)>2:
        draw2=True
        for n in range(0,2):
            hand.append(deck[0])
            del deck[0]

    if play[1]=="draw4" and len(deck)>4:
        draw4=True
        for n in range(0,4):
            hand.append(deck[0])
            del deck[0]

    #is skipped?

    if play[1] in skiplist:
        skip=True

    if play[1]=="sr":
        play[1]= "reverse"
    if play[1]=="s":
        play[1]= "skip"
        
    #numbers

    if skip==False:
        for n in hand:
            sp=n.rsplit(":")
            if play[1] in numstr:
                if play[0]==sp[0]:
                    ind=hand.index(n)
                    if ind in potind:
                        potind.remove(ind)
                    potind.append(ind)
                if play[1]==sp[1]:
                    ind=hand.index(n)
                    if ind in potind:
                        potind.remove(ind)
                    potind.append(ind)
            if play[0] in handcolours:
                if play[0]==sp[0]:
                    ind=hand.index(n)
                    if ind in potind:
                        potind.remove(ind)
                    potind.append(ind)
                if play[1]==sp[1]:
                    ind=hand.index(n)
                    if ind in potind:
                        potind.remove(ind)
                    potind.append(ind)
    
    #wild

    if play[0]==" ":
        potind=[]
        for n in range(0,len(hand)):
            potind.append(n)

    if skip==False and ind==-1:
        for n in hand:
            sp=n.rsplit(":")
            if sp[1] in wilds:
                ind=hand.index(n)
                if ind in potind:
                    potind.remove(ind)
                potind.append(ind)

    #draw

    if ind ==-1 and len(deck)>0:
        hand.append(deck[0])
        del deck[0]
        if not(skip):
            for n in hand:
                sp=n.rsplit(":")
                if play[1] in numstr:
                    if play[0]==sp[0]:
                        ind=hand.index(n)
                        if ind in potind:
                            potind.remove(ind)
                        potind.append(ind)
                    if play[1]==sp[1]:
                        ind=hand.index(n)
                        if ind in potind:
                            potind.remove(ind)
                        potind.append(ind)
                if play[0] in hand:
                    if play[0]==sp[0]:
                        ind=hand.index(n)
                        if ind in potind:
                            potind.remove(ind)
                        potind.append(ind)
                    if play[1]==sp[1]:
                        ind=hand.index(n)
                        if ind in potind:
                            potind.remove(ind)
                        potind.append(ind)
    #skip
    
    if play[1]=="s" and ind==-1:
        for n in hand:
            sp=n.rsplit(":")
            if play[0] ==sp[0] and sp[1]in skiplist:
                ind=hand.index(n)
                if ind in potind:
                    potind.remove(ind)
                potind.append(ind)

    #calculation
    print(potind)

    if ind!=-1 and skip!=True:
        ind=potind[random.randint(0,len(potind)-1)]

    for n in potind:
        c=hand[ind]
        c=c.rsplit(":")
        if numinlist(c[0],handcolours)>1 and c in skiplist:
            ind=n
            if (len(hand)<8 or len(hando)<8) and numinlist(c[0],handcolours)>2:
                break
        
        if (c[1]=="draw2" or c[1]=="draw4") and len(hando)<6:
            ind=n
            if len(hando)<5:
                break



    if skip==False and ind!=-1:
        card=hand[ind]
        del hand[ind]
    else:
        skip=True
    return card,hand,deck,skip

def newdeck(startdeal):
    deck=createdeck()
    hand1=deal(startdeal,deck)
    hand2=deal(startdeal,deck)
    return deck,hand1,hand2