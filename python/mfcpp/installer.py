from tkinter import Tk, simpledialog as spd, messagebox\
    as mbx,Canvas,HIDDEN,NORMAL
try:
    import urllib.request as url
except ImportError:
    import urllib as url
import os
root=Tk()
root.withdraw()
url.urlretrieve('https://mpfc-py.glitch.me/updateextention.py','updateextention.py')
url.urlretrieve('https://mpfc-py.glitch.me/mfcpp.py','mfcpp.py')
funcins=spd.askstring('download mathsextention?','press a to down\
load mathsextention press b if you do not want to download it')
if funcins=='a':
    url.urlretrieve('https://mpfc-py.glitch.me/mathextention.py','mathexte\
ntion.py')
funcins=spd.askstring('download graphextention?','press a to down\
load graphextention press b if you do not want to download it')
if funcins=='a':
    url.urlretrieve('https://mpfc-py.glitch.me/graphextention.py','graphext\
ention.py')
funcins=spd.askstring('download factorextention?','press a to down\
load factorextention press b if you do not want to download it')
if funcins=='a':
    url.urlretrieve('https://mpfc-py.glitch.me/factorextention.py','factorext\
ention.py')
    url.urlretrieve('https://mpfc-py.glitch.me/primes.txt','primes.txt')
funcins=spd.askstring('download websiteextention?','press a to down\
load websiteextention press b if you do not want to download it')
if funcins=='a':
    url.urlretrieve('https://mpfc-py.glitch.me/websiteextention.py','websiteex\
tention.py')
    url.urlretrieve('https://mpfc-py.glitch.me/websites.txt','websites.txt')
funcins=spd.askstring('download cryptextention?','press a to down\
load cryptextention press b if you do not want to download it')
if funcins=='a':
    url.urlretrieve('https://mpfc-py.glitch.me/cryptextention.py','cryptextent\
ion.py')
funcins=spd.askstring('download eventextention?','press a to down\
load eventextention press b if you do not want to download it')
if funcins=='a':
    url.urlretrieve('https://mpfc-py.glitch.me/eventextention.py','eventextent\
ion.py')
    url.urlretrieve('https://mpfc-py.glitch.me/events.txt','events.txt')
os.remove('mfcppinstaller.py')
