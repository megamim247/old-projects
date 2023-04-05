
try:
    import urllib.request as url
except ImportError:
    import urllib as url
x='https://cdn.glitch.me/56334c6f-f8b2-4770-9e06-803566fe4ec7%2Fbgwb1.png'
url.urlretrieve(x)
