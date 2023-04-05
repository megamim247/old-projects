import uno_max
import turtle
deck=uno_max.deck
hand1=uno_max.hand1
hand2=uno_max.hand2
plays=[]
numstr=["0","1","2","3","4","5","6","7","8","9"]
play=deck[0]
deckcount=999
hand1len=[]
hand2len=[]
del deck[0]
plays.append(play)
while not(play.rsplit(":")[1] in numstr):
    play=deck[0]
    del deck[0]
    plays.append(play)
print(play)
hand1len.append(len(hand1))
hand2len.append(len(hand2))

#main!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
while len(hand1)>0 and len(hand2)>0 and deckcount>0:
    while (len(hand1)>0 and len(hand2)>0) and len(deck)>0:

        # player1
        if len(hand2)>0:
            print(hand1)
            ((play,hand1,deck,skip))=uno_max.play1(hand1,hand2,play,deck)
            if skip ==False:
                plays.append(play)
                print(play)
            else:
                play=plays[-1].rsplit(":")
                if play[-1]=="skip":
                    play=play[0]+":ss"
                elif play[-1]=="reverse":
                    play=play[0]+":sr"
                else:
                    play=play[0]+":s"
                
                plays.append(play)
                print("skip")
            hand1len.append(len(hand1))
        # player2
        if len(hand1)>0:
            print(hand2)
            ((play,hand2,deck,skip))=uno_max.play2(hand2,hand1,play,deck)
            if skip ==False:
                plays.append(play)
                print(play)
            else:
                play=plays[-1].rsplit(":")
                if play[-1]=="skip":
                    play=play[0]+":ss"
                elif play[-1]=="reverse":
                    play=play[0]+":sr"
                else:
                    play=play[0]+":s"
                
                plays.append(play)
                print("skip")
            hand2len.append(len(hand2))
    deckcount-=1
    deck=uno_max.createnewdeck(hand1,hand2)
print(plays)
print(hand1len)
print(hand2len)


#graph
#smooth
fontsize=6
smoothhand1len=[]
smoothhand2len=[]
graphingspeed=0
graphwidth=4
rawwidth=1
t=turtle.Turtle()
t.penup()
t.speed(0)
funcbc1=len(hand1len)
funcbc2=1
funcbc3=1
funcbc4=len(hand1len)*funcbc2
funcbc5=20
xoffset=-960+2
yoffset=-520+2
sq=12
sqx=1920/len(hand1len)
for funcbc6 in range(funcbc5+1):
    t.goto(xoffset,sq*funcbc6+yoffset)
    t.pendown()
    t.write(funcbc3*funcbc6, font=( "Arial", fontsize, "normal"))

t.penup()

for funcbc7 in range(funcbc4+1):
    t.goto(sqx*funcbc7+xoffset,yoffset)
    t.pendown()
    t.write(funcbc2*funcbc7, font=( "Arial", fontsize, "normal"))

t.pensize(graphwidth)
t.penup()
t.color("red")
funcbc11=hand1len[0]
for funcbc8 in range(funcbc1):
    funcbc9=funcbc8
    funcbc10=hand1len[funcbc8]
    if funcbc8!=len(hand1len)-1:
        funcbc12=hand1len[funcbc8+1]
    for n in range(23):
        if funcbc10>funcbc11:
            funcbc10-=0.1*(23/(n+1))
        elif funcbc10<funcbc11:
            funcbc10+=0.1*(23/(n+1))

    for n in range(3):
        if funcbc12>funcbc10:
            funcbc12-=0.1*(2/(n+1))
        elif funcbc12<funcbc10:
            funcbc12+=0.1*(2/(n+1))

    funcbc10=(funcbc10+funcbc12+funcbc11)/3

    smoothhand1len.append(funcbc10)

    funcbc11=funcbc10
    t.goto(sqx*funcbc2*funcbc9+xoffset,sq*funcbc3*funcbc10+yoffset)
    t.speed(graphingspeed)
    t.pendown()

t.speed(0)
funcbc1=len(hand2len)
t.penup()
t.color("blue")
funcbc11=hand2len[0]
for funcbc8 in range(funcbc1):
    funcbc9=funcbc8
    funcbc10=hand2len[funcbc8]
    if funcbc8!=len(hand2len)-1:
        funcbc12=hand2len[funcbc8+1]
    for n in range(23):
        if funcbc10>funcbc11:
            funcbc10-=0.1*(23/(n+1))
        elif funcbc10<funcbc11:
            funcbc10+=0.1*(23/(n+1))

    for n in range(3):
        if funcbc12>funcbc10:
            funcbc12-=0.1*(2/(n+1))
        elif funcbc12<funcbc10:
            funcbc12+=0.1*(2/(n+1))

    funcbc10=(funcbc10+funcbc12+funcbc11)/3

    smoothhand2len.append(funcbc10)

    funcbc11=funcbc10
    t.goto(sqx*funcbc2*funcbc9+xoffset,sq*funcbc3*funcbc10+yoffset)
    t.speed(graphingspeed)
    t.pendown()

#raw
t.pensize(rawwidth)
t.speed(0)
t.penup()
t.color("red")
funcbc11=hand2len[0]
for funcbc8 in range(funcbc1):
    funcbc9=funcbc8
    funcbc10=hand1len[funcbc8]
    if funcbc10>funcbc11:
        funcbc10-=0.25
    elif funcbc10<funcbc11:
        funcbc10+=0.25
    funcbc11=hand1len[funcbc8]
    t.goto(sqx*funcbc2*funcbc9+xoffset,sq*funcbc3*funcbc10+yoffset)
    t.speed(graphingspeed)
    t.pendown()

t.speed(0)
funcbc1=len(hand2len)
t.penup()
t.color("blue")
funcbc11=hand2len[0]
for funcbc8 in range(funcbc1):
    funcbc9=funcbc8
    funcbc10=hand2len[funcbc8]
    funcbc11=hand2len[funcbc8]
    if funcbc10>funcbc11:
        funcbc10-=0.25
    elif funcbc10<funcbc11:
        funcbc10+=0.25
    t.goto(sqx*funcbc2*funcbc9+xoffset,sq*funcbc3*funcbc10+yoffset)
    t.speed(graphingspeed)
    t.pendown()

#hand ratio(objective closeness)
#raw
t.color("black")
graphingspeed=0
graphwidth=4
t.penup()
t.speed(0)
funcbc1=len(hand1len)
funcbc2=1
funcbc3=1
funcbc4=len(hand1len)*funcbc2
funcbc5=7
xoffset=-960+1
yoffset=-160+1
sq=12
ymultiplier=3
for funcbc6 in range(funcbc5+1):
    t.goto(xoffset,ymultiplier*sq*funcbc6+yoffset)
    t.pendown()
    t.write(funcbc3*funcbc6, font=( "Arial", fontsize, "normal"))

t.penup()

for funcbc7 in range(funcbc4+1):
    t.goto(sqx*funcbc7+xoffset,yoffset)
    t.pendown()
    t.write(funcbc2*funcbc7, font=( "Arial", fontsize, "normal"))



#raw

t.pensize(rawwidth)
t.penup()
t.color("red")

#lencheck
if len(hand2len)>len(hand1len):
    funcbc1=len(hand1len)
else:
    funcbc1=len(hand2len)
hand2rat=[]
funcbc11=hand2len[0]/hand1len[0]
for funcbc8 in range(funcbc1):
    funcbc9=funcbc8
    if hand1len[funcbc8]!=0:
        funcbc10=hand2len[funcbc8]/hand1len[funcbc8]
        hand2rat.append(funcbc10)
    else:
        funcbc10=7

    if funcbc10>funcbc11:
        funcbc10-=0.5
    elif funcbc10<funcbc11:
        funcbc10+=0.5

    funcbc11=hand1len[funcbc8]
    t.goto(sqx*funcbc2*funcbc9+xoffset,ymultiplier*sq*funcbc3*funcbc10+yoffset)
    t.speed(graphingspeed)
    t.pendown()

#lencheck
hand1rat=[]
if len(hand1len)>len(hand2len):
    funcbc1=len(hand2len)
else:
    funcbc1=len(hand1len)

t.pensize(rawwidth)
t.penup()
t.color("blue")
funcbc11=hand1len[0]/hand2len[0]
for funcbc8 in range(funcbc1):
    funcbc9=funcbc8
    if hand2len[funcbc8]!=0:
        funcbc10=hand1len[funcbc8]/hand2len[funcbc8]
        hand1rat.append(funcbc10)
    else:
        funcbc10=7

    if funcbc10>funcbc11:
        funcbc10-=0.5
    elif funcbc10<funcbc11:
        funcbc10+=0.5

    funcbc11=hand2len[funcbc8]
    t.goto(sqx*funcbc2*funcbc9+xoffset,ymultiplier*sq*funcbc3*funcbc10+yoffset)
    t.speed(graphingspeed)
    t.pendown()

#hand +/-
#raw
t.color("black")
graphingspeed=0
graphwidth=4
t.penup()
t.speed(0)
funcbc1=len(hand1len)
funcbc2=1
funcbc3=1
funcbc4=len(hand1len)*funcbc2
funcbc5=12
xoffset=-960+1
yoffset=340+1
sq=12
ymultiplier=0.9
for funcbc6 in range(funcbc5+1):
    t.goto(xoffset,ymultiplier*sq*funcbc6+yoffset)
    t.pendown()
    t.write(funcbc3*funcbc6, font=( "Arial", fontsize, "normal"))

t.penup()

for funcbc7 in range(funcbc4+1):
    t.goto(sqx*funcbc7+xoffset,yoffset)
    t.pendown()
    t.write(funcbc2*funcbc7, font=( "Arial", fontsize, "normal"))

#raw

t.pensize(rawwidth)
t.penup()
t.color("red")

#lencheck
if len(hand2len)>len(hand1len):
    funcbc1=len(hand1len)
else:
    funcbc1=len(hand2len)

funcbc11=uno_max.startdeal
for funcbc8 in range(funcbc1):
    funcbc9=funcbc8
    if hand1len[funcbc8]!=0:
        funcbc10=hand2len[funcbc8]-hand1len[funcbc8]
    else:
        funcbc10=7

    if funcbc10>funcbc11:
        funcbc10-=0.25
    elif funcbc10<funcbc11:
        funcbc10+=0.25
    
    if int(t.ycor())<340:
        t.color("blue")
    if int(t.ycor())>340:
        t.color("red")

    funcbc11=hand1len[funcbc8]
    t.goto(sqx*funcbc2*funcbc9+xoffset,ymultiplier*sq*funcbc3*funcbc10+yoffset)
    t.speed(graphingspeed)
    t.pendown()

#useful(subjective closeness/farness?) current(12)

subcloseness=12
t.pensize(graphwidth)
t.penup()
t.color("red")

#lencheck
if len(hand2rat)>len(hand1rat):
    funcbc1=len(hand1rat)
else:
    funcbc1=len(hand2rat)

funcbc11=uno_max.startdeal
for funcbc8 in range(funcbc1):
    funcbc9=funcbc8
    if hand1len[funcbc8]!=0:
        funcbc10=hand2len[funcbc8]-hand1len[funcbc8]
    else:
        funcbc10=7

    if funcbc10>funcbc11 and hand2rat[funcbc8]!=0:
        funcbc10-=0.25
        funcbc10=(funcbc10/subcloseness)*hand2rat[funcbc8]
    elif funcbc10<funcbc11 and hand1rat[funcbc8]!=0:
        funcbc10+=0.25
        funcbc10=(funcbc10/subcloseness)*hand1rat[funcbc8]
    
    if int(t.ycor())<340:
        t.color("blue")
    if int(t.ycor())>340:
        t.color("red")

    funcbc11=hand1len[funcbc8]
    t.goto(sqx*funcbc2*funcbc9+xoffset,ymultiplier*sq*funcbc3*funcbc10+yoffset)
    t.speed(graphingspeed)
    t.pendown()

#end
while True:
    t.penup()
    t.goto(0,0)