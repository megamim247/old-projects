import uno_max
import turtle
#const
numstr=["0","1","2","3","4","5","6","7","8","9"]
results=5

databasehand1len=[]
databasehand2len=[]
databaseplays=[]

#loop:
for n in range(results):
    deckcount=999
    deck,hand1,hand2=uno_max.newdeck(uno_max.startdeal)
    #database
    plays=[]
    hand1len=[]
    hand2len=[]
    #startup
    play=deck[0]
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
    databasehand1len.append(hand1len)
    databasehand2len.append(hand2len)
    databaseplays.append(plays)

print(databasehand1len)
print(databasehand2len)
print(databaseplays)
#graph
#smooth
fontsize=6
smoothhand1len=[]
smoothhand2len=[]
graphingspeed=0
graphwidth=7
rawwidth=1
t=turtle.Turtle()
t.penup()
t.speed(0)
length=150
funcbc1=length
funcbc2=1
funcbc3=1
funcbc4=length*funcbc2
funcbc5=20
xoffset=-960+2
yoffset=-520+2
sq=12
sqx=1920/length
for funcbc6 in range(funcbc5+1):
    t.goto(xoffset,sq*funcbc6+yoffset)
    t.pendown()
    t.write(funcbc3*funcbc6, font=( "Arial", fontsize, "normal"))

t.penup()

for funcbc7 in range(funcbc4+1):
    t.goto(sqx*funcbc7+xoffset,yoffset)
    t.pendown()
    t.write(funcbc2*funcbc7, font=( "Arial", fontsize, "normal"))
for n in range(len(databasehand1len)):
    t.pensize(graphwidth)
    t.penup()
    t.color("red")
    hand1len=databasehand1len[n]
    funcbc11=hand1len[0]
    for funcbc8 in range(funcbc1):
        funcbc9=funcbc8
        try:
            funcbc10=hand1len[funcbc8]
        except:
            break
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

for n in range(len(databasehand2len)):
    t.pensize(graphwidth)
    t.penup()
    t.color("blue")
    hand1len=databasehand2len[n]
    funcbc11=hand1len[0]
    for funcbc8 in range(funcbc1):
        funcbc9=funcbc8
        try:
            funcbc10=hand1len[funcbc8]
        except:
            break
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

#end
while True:
    t.penup()
    t.goto(0,0)