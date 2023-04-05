import urllib.request
import re
#put url here|||||||||||||||||||||||||||||||||||||||
url1="https://www.timeanddate.com/weather/united-arab-emirates/sharjah"
#|||||||||||||||||||||||||||||||||||||||||||||||||||
def remstri(i, s):
    return s[:i] + s[i+1:]
def urlrd(url):
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
    xe=re.search(r'<div class="change__value(.*?)</div>',rd)
    
    return xe[1]
def urlre(url):
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
    xe=re.search(r'<div class="change__percent(.*?)</div>',rd)
    
    return xe[1]
def urlrp(url):
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
    xe=re.search(r'<div class="quote__close(.*?)</div>',rd)
    
    return xe[1]
urlpr=urlrp(url1)
while True:
    urpr=urlrp(url1)
    if urpr!=urlpr:
        print(urpr)
        urlpr=urpr

