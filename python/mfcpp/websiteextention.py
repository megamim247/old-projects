import webbrowser
from tkinter import Tk, simpledialog as spd, messagebox\
     as mbx,Canvas,HIDDEN,NORMAL
import urllib.request
import re
def remstri(i, s):
    return s[:i] + s[i+1:]
def urlrd(url1):
    x=0
    rd=urllib.request.urlopen(url1)
    rd=rd.read()
    #change website encoding
    rd=rd.decode("utf-8")
    #make this line a comment if u want see the head tag content
    rd=re.sub('<head(.*?)/head>', '', rd, flags=re.DOTALL)
    #make this line a comment if u want see the script tag content
    rd=re.sub('<script(.*?)/script>', '', rd, flags=re.DOTALL)
    #make this line a comment if u want see the url content
    rd=re.sub('src="(.*?)"', '', rd, flags=re.DOTALL)
    rd=re.sub('href="(.*?)"', '', rd, flags=re.DOTALL)
    # make this a comment if u want to see the detail content
    rd=re.sub('="(.*?)"', '', rd, flags=re.DOTALL)
    # make this a comment if u want to see the detail content
    rd=re.sub('=\'(.*?)\'', '', rd, flags=re.DOTALL)
    rd=re.sub('<.*?>', '', rd)
    rd=rd.replace('<br', '')
    rd=rd.replace('<span', '')
    rd=rd.replace('</span', '')
    rd=rd.replace('<button', '')
    rd=rd.replace('</button', '')
    rd=rd.replace('<!DOCTYPE', '')
    rd=rd.replace('<html', '')
    rd=rd.replace('</html', '')
    rd=rd.replace('<title', '')
    rd=rd.replace('</title', '')
    rd=rd.replace('<div', '')
    rd=rd.replace('</div', '')
    rd=rd.replace('<h1', '')
    rd=rd.replace('</h1', '')
    rd=rd.replace('<h2', '')
    rd=rd.replace('</h2', '')
    rd=rd.replace('<h3', '')
    rd=rd.replace('</h3', '')
    rd=rd.replace('<h4', '')
    rd=rd.replace('</h4', '')
    rd=rd.replace('<a', '')
    rd=rd.replace('</a', '')
    rd=rd.replace('<p', '')
    rd=rd.replace('</p', '')
    rd=rd.replace('/>', '')
    rd=rd.replace('<', '')
    rd=rd.replace('>', '')
    rd=rd.replace('&nbsp;', '')
    rd=rd.replace('&amp;', '')
    rd=re.sub('&#(.*?);', '', rd, flags=re.DOTALL)
    for x in range(10):
        rd=rd.replace('\n\n', '\n')
        rd=rd.replace('\n \n', '\n')
        rd=rd.replace('  ', '')
        rd=rd.replace('\t', '')
        rd=rd.replace('\r\n', '\n')
    return rd
funcfa=''
b=[]
root = Tk()
def writfil(a):
    with open("websites.txt",'a')as file:
        file.write(','+a)
a=open("websites.txt" , "r")
a=a.read()
b=a.split(',')
print(b)
fq='would u like to:'
while True:
    funcfa=spd.askstring('website',fq+'a veiw websites b add websites c veiw website in pythin')
    if funcfa=='a':
        #funcfaa
        funcfaa=spd.askinteger('website',fq+'type in website number')
        webbrowser.open(b[funcfaa-1])
    elif funcfa=='b':
        #funcfab
        funcfab=spd.askstring('website',fq+'type in website url')
        writfil(funcfab)
    elif funcfa=='c':
        #funcfac
        funcfac=spd.askstring('website','please type in website url')
        rdweb=urlrd(funcfac)
        print(rdweb)
