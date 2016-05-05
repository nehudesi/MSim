import urllib

def wget2(url):
  try:
    ufile = urllib.urlopen(url)
    print ufile.read()
  except IOError:
    print 'problem reading url:', url
    
    
    
url = "http://finance.yahoo.com/"
wget2(url)
