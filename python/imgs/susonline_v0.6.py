#imports
import pygame
import socket
import threading
#font
pygame.font.init()
font=pygame.font.SysFont("comicsans",40)

#FPS
FPS=60
#borderx
borderxobject=[]
borderxx=[0,100,300,150,300,0,500]
borderxy=[900,900,790,680,570,570,570]
borderxsizex=100
borderxsizey=10

#bordery
borderyobject=[]
borderyx=[200,300]
borderyy=[900,470]
borderysizex=10
borderysizey=100

#start variables

#counters
gravity=1
x=0
x2=0

#boolean
left=False
run=True
jump=False
collideb=False
collider=False
collidel=False

#colour
WHITE=((255,255,255))
BLACK=((0,0,0))

#events:
guyhit=pygame.USEREVENT+1
otherguyhit=pygame.USEREVENT+2
#objects

#window
WIDTH,HEIGHT=1200,1000
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("sus online")
#guy
otherguyx=0
otherguyy=0
oldotherguyx=0
oldotherguyy=0
otherguyleft=False
GUY=pygame.image.load("amogus.png")
guyx,guyy=20,30
GUYF=pygame.transform.flip(GUY, True, False)
guy=pygame.Rect(100,800,guyx,guyy)
guyb=pygame.Rect(100,100,guyx,guyy-20)
guyr=pygame.Rect(100,100,guyx-10,guyy)
guyl=pygame.Rect(100,100,guyx-10,guyy)
otherguy=pygame.Rect(100,800,guyx,guyy)
#game objects
#mirror
mirror=True
if mirror:
    for n in range(len(borderxx)):
        borderxx.append(WIDTH-borderxx[n]-borderxsizex)
        borderxy.append(borderxy[n])
    for n in range(len(borderyx)):
        borderyx.append(WIDTH-borderyx[n]-borderysizex)
        borderyy.append(borderyy[n])
#borderx
for n in range(len(borderxx)):
    borderxobject.append(pygame.Rect(borderxx[n-1],borderxy[n-1],borderxsizex,borderxsizey))
#bordery
for n in range(len(borderyx)):
    borderyobject.append(pygame.Rect(borderyx[n-1],borderyy[n-1],borderysizex,borderysizey))
#bullet:
shoot="0000"
bulletvel=20
bullets=[]
bulletdirection=[]
hits=0
otherguybullets=[]
otherguybulletdirection=[]
otherguyhits=0
numofbullets=6
def handle_bullets():
    global otherguyhits
    global hits
    #guy
    for bullet in bullets:
        b_num=bullets.index(bullet)
        if bulletdirection[b_num]:
            bullet.x -= bulletvel
        else:
            bullet.x += bulletvel
        if otherguy.colliderect(bullet):
            bullets.remove(bullet)
            del bulletdirection[b_num]
            hits+=1
        elif bullet.x > WIDTH or bullet.x<0:
            bullets.remove(bullet)
            del bulletdirection[b_num]
        for n in range(len(borderyx)):
            if borderyobject[n].colliderect(bullet):
                bullets.remove(bullet)
                del bulletdirection[b_num]

    #otherguy
    for bullet in otherguybullets:
        b_num=otherguybullets.index(bullet)
        if otherguybulletdirection[b_num]:
            bullet.x -= bulletvel
        else:
            bullet.x += bulletvel
        if guy.colliderect(bullet):
            otherguybullets.remove(bullet)
            del otherguybulletdirection[b_num]
            otherguyhits+=1
        elif bullet.x > WIDTH or bullet.x<0:
            otherguybullets.remove(bullet)
            del otherguybulletdirection[b_num]
        for n in range(len(borderyx)):
            if borderyobject[n].colliderect(bullet):
                otherguybullets.remove(bullet)
                del otherguybulletdirection[b_num]

#clock
clock = pygame.time.Clock()

#physics
vel=5
aclgravity=0.14
jlength=35
j=6

#client
PORT=5050 
PORT2=5055
SERVER="192.168.1.128"
ADDR=(SERVER,PORT)
first=True

HEADER=9
FORMAT="utf-8"


#movement setup
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

#send
def send(msg):
    client.send(msg.encode(FORMAT))
#receive
def receive():
    global otherguyx
    global otherguyy
    global otherguyleft
    first=client.recv(HEADER).decode(FORMAT)
    while True:
        msg=client.recv(HEADER).decode(FORMAT)
        msg2=client.recv(HEADER).decode(FORMAT)
        if len(msg)>3:
            if int(msg)<2000:
                otherguyx=int(msg)
                otherguyy=int(msg2)
            else:
                msg=msg[3:]
                if msg[0]=="1":
                    bullet=pygame.Rect(otherguy.x,(otherguy.y+otherguy.height//2),15,4)
                    otherguybullets.append(bullet)
                    otherguybulletdirection.append(otherguyleft)
                msg=msg[1:]
                otherguyx=int(msg)
                otherguyy=int(msg2)
        else:
            if int(msg2)<2000:
                otherguyx=int(msg2)
                otherguyy=int(msg)
            else:
                msg2=msg2[3:]
                if msg2[0]=="1":
                    bullet=pygame.Rect(otherguy.x,(otherguy.y+otherguy.height//2),15,4)
                    otherguybullets.append(bullet)
                    otherguybulletdirection.append(otherguyleft)
                msg2=msg2[1:]
                otherguyx=int(msg2)
                otherguyy=int(msg)
        
thread=threading.Thread(target=receive)
thread.start()
#main
while run:
    #tick
    clock.tick(FPS)

    #BG
    WIN.fill(WHITE)
    for n in range(len(borderxx)):
        pygame.draw.rect(WIN,BLACK,borderxobject[n])
    for n in range(len(borderyx)):
        pygame.draw.rect(WIN,BLACK,borderyobject[n])
        WIN.blit((font.render(str(hits),1,BLACK)),(10,10))
        WIN.blit((font.render(str(otherguyhits),1,BLACK)),(WIDTH-100,10))
    
    #blit1
    if otherguyx<oldotherguyx:
        otherguyleft=True
    if otherguyx>oldotherguyx:
        otherguyleft=False
    if otherguyleft:
        WIN.blit(GUYF,(otherguyx,otherguyy))
    else:
        WIN.blit(GUY,(otherguyx,otherguyy))
    
    #events
    for event in pygame.event.get():

        #quit
        if event.type==pygame.QUIT:
            run = False
        
        #shooting:
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and int(len(bullets))<int(numofbullets):
                bullet=pygame.Rect(guy.x,(guy.y+guy.height//2),15,4)
                bullets.append(bullet)
                bulletdirection.append(left)
                shoot="1111"
            else:
                shoot="0000"
        else:
            shoot="0000"

    #collision y
    guyb.x=guy.x
    guyb.y=guy.y+20
    collideb=False
    for n in range(len(borderxx)):
        while borderxobject[n].colliderect(guyb):
            collideb=True
            guy.y-=1
            guyb.y-=1
            gravity=0.2

    #movement    
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_a] and guy.x-vel>0:
        guy.x-=vel
        left=True
    if pressed[pygame.K_d] and guy.x+vel+20<WIDTH:
        guy.x+=vel
        left=False
    if pressed[pygame.K_w] and (guy.y+29>HEIGHT or collideb):
        x=jlength
        jump=True
        collideb=False
    if pressed[pygame.K_SPACE] and int(len(bullets))<int(numofbullets):
        bullet=pygame.Rect(guy.x,(guy.y+guy.height//2),15,4)
        bullets.append(bullet)
        bulletdirection.append(left)
        shoot="1111"
    else:
        shoot="0000"
    
    #shooting:
    handle_bullets()
    for bullet in bullets:
        pygame.draw.rect(WIN,BLACK,bullet)
    for bullet in otherguybullets:
        pygame.draw.rect(WIN,BLACK,bullet)

    
    #collision x
    guyr.x=guy.x+10
    guyl.y=guyr.y=guy.y
    guyl.x=guy.x
    for n in range(len(borderyx)):
        while borderyobject[n].colliderect(guyr):
            collider=True
            guy.x-=1
            guyr.x-=1
        while borderyobject[n].colliderect(guyl):
            collidel=True
            guy.x+=1
            guyl.x+=1
  
    #jump
    if jump and x>0:
        if pressed[pygame.K_w]:
            guy.y-=j
        else:
            x=2
        x-=1
    else:
        jump=False
    if x==1:
        gravity=0.6
        x=0
    

    #gravity
    while guy.y+29>HEIGHT:
        gravity=0
        guy.y-=1
    else:
        guy.y+=gravity

    gravity+=aclgravity
    g=True

    #online:
    send(str(shoot)+str(guy.x))
    send(str(int(guy.y)))

    #finalblit
    if left:
        WIN.blit(GUYF,(guy.x,guy.y))
    else:
        WIN.blit(GUY,(guy.x,guy.y))
    #blit2
    if otherguyx<oldotherguyx:
        otherguyleft=True
    if otherguyx>oldotherguyx:
        otherguyleft=False
    if otherguyleft:
        WIN.blit(GUYF,(otherguyx,otherguyy))
    else:
        WIN.blit(GUY,(otherguyx,otherguyy))
    otherguy.x=otherguyx
    otherguy.y=otherguyy
    oldotherguyx=otherguyx
    pygame.display.update()
pygame.quit()
