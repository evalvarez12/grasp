# -*- coding: UTF-8 -*-

import re


titleRegex = re.compile(r'<title>([a-zA-Z0-9ñÑ]+)<\\title>',re.UNICODE)

wordSpecsRegex = re.compile(r'== ?\{\{([a-zA-ZñÑ]+\|.*)\}\} ?==',re.UNICODE)

#cleanWordsRegex = re.compile()




#def findWordSpecs(line) :
    #p = re.compile(r'==([a-zA-Z0-9ñÑ]+)==',re.UNICODE)
    #m = p.match(word)
    #if m :
	#return m.group(1)
    #else
	#return ''
    
    
#def cleanContents(line) :
    




#def findTitle(line) :
    #p = re.compile(r'<title>([a-zA-Z0-9ñÑ])<\\title>',re.UNICODE)
    #m = p.match(doc)
    #if m :
	#return m.group(1)
    #else :
	#return None
    
    
