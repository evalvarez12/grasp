# -*- coding: UTF-8 -*-

import re


title_re = re.compile(r'<title>([^\W\d_]+)<\\title>',re.UNICODE)

word_specs_re = re.compile(r'== ?\{\{([^\W\d_]+)\|([^\W\d_]+)\}\} ?==',re.UNICODE)

word_replace1_re = re.compile(r'\{\{plm\|([^\W\d_]+)\}\}')

word_replace2_re = re.compile(r'\[\[([^\W\d_]+)\]\]')

number_replace_re = re.compile(r';(\d+):')

clear = re.compile(r'\{\{clear\}\}')


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
    
    
