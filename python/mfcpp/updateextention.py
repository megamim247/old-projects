try:
    import urllib.request as url
except ImportError:
    import urllib as url
import os
url.urlretrieve('https://mpfc-py.glitch.me/mathextention.py','mathexte\
ntion.py')
os.remove('mfcpp.py')
url.urlretrieve('https://mpfc-py.glitch.me/mfcpp.py','mfcpp.py')
if os.path.exists('mathextention.py'):
    os.remove('mathextention.py')
    url.urlretrieve('https://mpfc-py.glitch.me/mathextention.py','mathexte\
ntion.py')
if os.path.exists('graphextention.py'):
    os.remove('graphextention.py')
    url.urlretrieve('https://mpfc-py.glitch.me/graphextention.py','graphext\
ention.py')
if os.path.exists('factorextention.py'):
    os.remove('factorextention.py')
    url.urlretrieve('https://mpfc-py.glitch.me/factorextention.py','factorext\
ention.py')
if os.path.exists('websiteextention.py'):
    os.remove('websiteextention.py')
    url.urlretrieve('https://mpfc-py.glitch.me/websiteextention.py','websiteex\
tention.py')
if os.path.exists('cryptextention.py'):
    os.remove('cryptextention.py')
    url.urlretrieve('https://mpfc-py.glitch.me/cryptextention.py','cryptextent\
ion.py')
if os.path.exists('eventextention.py'):
    os.remove('eventextention.py')
    url.urlretrieve('https://mpfc-py.glitch.me/eventextention.py','eventextent\
ion.py')
print('update completed!')