import urllib2
import extract as ext




def getSynonims(word) :
    url='http://www.diccionariodesinonimos.es/' + word + '/'
    response = urllib2.urlopen(url)
    html = response.read()
    
    
    
    
def findSynonims(data) :
    if data.count('<li class="synsetlist">') :
	start = data.find('<li class="synsetlist">') + 23
	end = data.find('</ul>') + 5
	findSynonims(data[start:end])
    else :
	processed = ext.processLine(data)