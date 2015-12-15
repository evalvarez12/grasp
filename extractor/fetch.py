import urllib2
import extract as ext




def getSynonims(word) :
    url='http://www.diccionariodesinonimos.es/' + word + '/'
    response = urllib2.urlopen(url)
    html = response.read()
    print url
    return findSynonims(html)
    
    
    
    
def findSynonims(data) :
    if data.count('<li class="synsetlist">') :
	start = data.find('<li class="synsetlist">') + 23
	end = data.find('</ul>') - 1
	return findSynonims(data[start:end])
    elif :
	start = data.find('http://www.diccionariodesinonimos.es/') + 37
	new = data[start:]
	end = new.find('/')
	word = data[:end]
	return getSynonims(word)
    else :
        return ext.processLine(data)	