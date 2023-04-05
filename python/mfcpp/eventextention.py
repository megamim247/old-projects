from tkinter import Tk, simpledialog as spd, messagebox\
     as mbx,Canvas,HIDDEN,NORMAL
from datetime import date,datetime
fq='would u like to:'
funcda1=100
root = Tk()
def writfil(a,b,c):
    with open(c,'a')as file:
        file.write('\n'+a+','+b)
def geteve():
    lieve=[]
    with open('events.txt') as file:
        for line in file:
            line=line.rstrip('\n')
            cueve=line.split(',')
            eveda=datetime.strptime(cueve[1],'%d/%m/%y').date()
            cueve[1]=eveda
            lieve.append(cueve)
    return lieve
def dabetda(da1,da2):
    timbet=str(da1-da2)
    numda=timbet.split(' ')
    return numda[0]
while True:
    for n in range(1):
        funcd=spd.askstring('events',fq+'a veiw events b add events')
        if funcd=='a':
            #funcda
            funcdc=Canvas(root,height=800,width=800,bg='indian red')
            funcdc.pack()
            funcdaeves=geteve()
            funcdatod=date.today()
            for funcdaeve in funcdaeves:
                funcdaevenm=funcdaeve[0]
                funcdadaun=dabetda(funcdaeve[1],funcdatod)
                funcdadis='it is %s days until %s'%(funcdadaun,\
                                                    funcdaevenm)
                funcdc.create_text(10,funcda1,anchor='w',fill='\
green',\
                                   font='Arial 20 bold',text=\
                                   funcdadis)
                funcda1=funcda1+30
        elif funcd=='b':
            #funcdb
            funcdb1=spd.askstring('add events','enter name in')
            funcdb2=spd.askstring('add events','enter date in d/m/y')
            writfil(funcdb1,funcdb2,'events.txt')
