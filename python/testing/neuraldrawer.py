

layers=[2,2,2]
biases=[-0.5,0.5,0,-0.25]
weights=[1,-1,-0.75,0.75,-0.25,0.25,0,0.1]
def drawneural(layers,biases,weights):
    import turtle as t
    t.speed("fastest")
    scale=2
    biasscale=30
    biasoffset=0
    for n in range(0,layers[0]):
        biases.insert(0,0)
    resolution=(1400/scale,720/scale)
    xoffset=resolution[0]/2
    yoffset=-resolution[1]/2
    xjump=resolution[0]/(len(layers))
    t.penup()
    numberofbiaspassed=0
    coords=[]
    #bias
    for n in range(0,len(layers)):
        yjump=-resolution[1]/(layers[n])
        coords2=[]
        layeryoffset=yjump/2
        for i in range(layers[n]):
            t.goto(n*xjump-xoffset,i*yjump-yoffset+layeryoffset)
            if (biases[numberofbiaspassed]*biasscale)<0:
                t.color("red")
            elif (biases[numberofbiaspassed]*biasscale)==0:
                t.color("blue")
            else:
                t.color("black")
            coords2.append((t.xcor(),t.ycor()+layeryoffset))
            t.goto(t.xcor(),t.ycor()+-abs(biases[numberofbiaspassed]*biasscale*(1)+biasoffset)+layeryoffset)
            t.pendown()
            t.begin_fill()
            t.circle(abs(biases[numberofbiaspassed]*biasscale+biasoffset))
            t.end_fill()
            t.penup()
            numberofbiaspassed=numberofbiaspassed+1
        coords.append(coords2)

    #weights
    curweight=0
    weightscale=20
    t.penup()
    t.speed(4) #debug
    t.pencolor("green")
    for n in range(1,len(layers)):
        for i in range(0,layers[n]):
            for ii in range(0,layers[i-1]+1):
                t.goto(coords[n][i][0],coords[n][i][1])
                if curweight<len(weights)+1:
                    t.pensize(abs(weights[curweight-3]*weightscale))
                t.pendown()
                if ii<=(len(coords[n-1])-1):
                    t.goto(coords[n-1][ii][0],coords[n-1][ii][1])
                t.penup()
                curweight=curweight+1


    t.penup()
    numberofbiaspassed=0
    coords=[]
    t.pensize(4)
    #bias
    for n in range(0,len(layers)):
        yjump=-resolution[1]/(layers[n])
        coords2=[]
        layeryoffset=yjump/2
        for i in range(layers[n]):
            t.goto(n*xjump-xoffset,i*yjump-yoffset+layeryoffset)
            if (biases[numberofbiaspassed]*biasscale)<0:
                t.color("red")
            elif (biases[numberofbiaspassed]*biasscale)==0:
                t.color("blue")
            else:
                t.color("black")
            coords2.append((t.xcor(),t.ycor()+layeryoffset))
            t.goto(t.xcor(),t.ycor()+-abs(biases[numberofbiaspassed]*biasscale*(1)+biasoffset)+layeryoffset)
            t.pendown()
            t.begin_fill()
            t.circle(abs(biases[numberofbiaspassed]*biasscale+biasoffset))
            t.end_fill()
            t.penup()
            numberofbiaspassed=numberofbiaspassed+1
        coords.append(coords2)
    t.mainloop()

    #debug
    print(coords)
if __name__ == '__main__':
    import threading
    t1=threading.Thread(target=drawneural,args=(layers,biases,weights,))
    t1.start()
    t1.join()
    t2=threading.Thread(target=drawneural,args=(layers,biases,weights,))
    t2.start()
    c=0
    while True:
        c=c+1
        print(c)
