import urllib2





def getSynonims(word) :
    response = urllib2.urlopen('http://www.example.com/')
html = response.read()