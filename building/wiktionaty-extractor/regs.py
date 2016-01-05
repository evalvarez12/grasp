# -*- coding: UTF-8 -*-
import re


title_re = re.compile(r'<title>([^\W\d_]+)</title>',re.UNICODE)

word_specs_re = re.compile(r'==\s?\{\{([^\W\d_]+)\|([^\W\d_]+)\}\}\s?==',re.UNICODE)

word_replace1_re = re.compile(r'\{\{plm\|([^\W\d_]+)\}\}')

word_replace2_re = re.compile(r'\[\[([^\W\d_]+)\]\]')

number_replace_re = re.compile(r';(\d+):')

clear_re = re.compile(r'\{\{clear\}\}')



def find_title(line) :
    m = title_re.search(line)
    if m :
	return m.group(1)
    else :
	return None
    
    
def find_word_specs(line) :
    m = word_specs_re.search(line)
    if m :
	return [m.group(1),m.group(2)]
    else :
	return None
    
    




#def findWordSpecs(line) :
    #p = re.compile(r'==([a-zA-Z0-9ñÑ]+)==',re.UNICODE)
    #m = p.match(word)
    #if m :
	#return m.group(1)
    #else
	#return ''
    
    
#def cleanContents(line) :
    




