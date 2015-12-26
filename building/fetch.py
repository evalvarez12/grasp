# -*- coding: UTF-8 -*-
import urllib2
import extractor.extract as ext




def getSynonims(word) :
    url='http://www.diccionariodesinonimos.es/' + word + '/'
    response = urllib2.urlopen(url)
    html = response.read()
    print url
    res = findSynonims(html)
    print res
    return res
    
    
    
def findSynonims(data) :
    unwanted = ['<ul class="compact">','<li class="synsetlist">','<strong>','</strong>','</ul>','</li>']
    if data.count('<ul class="compact">') :
	start = data.find('<ul class="compact">')
	end = data.find('</ul>') - 1
	synonims = data[start:end]
	for i in unwanted :
	    synonims = synonims.replace(i,"")
    else :
	start = data.find(' de" href="http://www.diccionariodesinonimos.es/') + 48
	new_word = data[start:]
	end = new_word.find('/')
	new_word = new_word[:end]
	synonims = getSynonims(new_word)
    
    return ext.processText(synonims)	