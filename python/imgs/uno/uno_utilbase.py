import random
#datacreate
data=[]
numstr=["0","1","2","3","4","5","6","7","8","9"]
startdeal=7
i=0
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
def deal():
    global startdeal
    global deck
    hand=[]
    for n in range(startdeal):
        hand.append(deck[n])
        del deck[n]
    return hand

def play1(hand,play,deck):
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

    #numbers

    if not(skip):
        for n in hand:
            sp=n.rsplit(":")
            if play[1] in numstr:
                if play[0]==sp[0]:
                    if ind in potind:
                        potind.remove(ind)
                    ind=hand.index(n)
                    potind.append(ind)
                if play[1]==sp[1]:
                    ind=hand.index(n)
                    if ind in potind:
                        potind.remove(ind)
                    ind=hand.index(n)
                    potind.append(ind)
            if play[0] in hand:
                if play[0]==sp[0]:
                    ind=hand.index(n)
                    if ind in potind:
                        potind.remove(ind)
                    ind=hand.index(n)
                    potind.append(ind)
                if play[1]==sp[1]:
                    ind=hand.index(n)
                    if ind in potind:
                        potind.remove(ind)
                    ind=hand.index(n)
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
                ind=hand.index(n)
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
                        ind=hand.index(n)
                        potind.append(ind)
                    if play[1]==sp[1]:
                        ind=hand.index(n)
                        if ind in potind:
                            potind.remove(ind)
                        ind=hand.index(n)
                        potind.append(ind)
                if play[0] in hand:
                    if play[0]==sp[0]:
                        ind=hand.index(n)
                        if ind in potind:
                            potind.remove(ind)
                        ind=hand.index(n)
                        potind.append(ind)
                    if play[1]==sp[1]:
                        ind=hand.index(n)
                        if ind in potind:
                            potind.remove(ind)
                        ind=hand.index(n)
                        potind.append(ind)
    #skip
    
    if play[1]=="s" and ind==-1:
        for n in hand:
            sp=n.rsplit(":")
            if play[0] ==sp[0] and sp[1]in skiplist:
                ind=hand.index(n)
                if ind in potind:
                    potind.remove(ind)
                ind=hand.index(n)
                potind.append(ind)
    print(potind)


    if skip==False and ind!=-1:
        card=hand[ind]
        del hand[ind]
    else:
        skip=True
    return card,hand,deck,skip

def play2(hand,play,deck):
    numstr=["0","1","2","3","4","5","6","7","8","9"]
    skiplist=["wild","draw4","skip","reverse"]
    wilds=["wild","draw4"]
    play=play.rsplit(":")
    ind=-1
    skip=False
    draw2=False
    draw4=False
    card=""
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

    #numbers

    if not(skip):
        for n in hand:
            sp=n.rsplit(":")
            if play[1] in numstr:
                if play[0]==sp[0]:
                    ind=hand.index(n)
                if play[1]==sp[1]:
                    ind=hand.index(n)
            if play[0] in hand:
                if play[0]==sp[0]:
                    ind=hand.index(n)
                if play[1]==sp[1]:
                    ind=hand.index(n)
    
    #wild

    if play[0]==" ":
        ind=random.randint(0,len(hand)-1)

    if skip==False and ind==-1:
        for n in hand:
            sp=n.rsplit(":")
            if sp[1] in wilds:
                ind=hand.index(n)

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
                    if play[1]==sp[1]:
                        ind=hand.index(n)
                if play[0] in hand:
                    if play[0]==sp[0]:
                        ind=hand.index(n)
                    if play[1]==sp[1]:
                        ind=hand.index(n)
    #skip
    
    if play[1]=="s" and ind==-1:
        for n in hand:
            sp=n.rsplit(":")
            if play[0] ==sp[0]:
                ind=hand.index(n)

    if skip==False and ind!=-1:
        card=hand[ind]
        del hand[ind]
    else:
        skip=True
    return card,hand,deck,skip

deck=createdeck()
hand1=deal()
hand2=deal()