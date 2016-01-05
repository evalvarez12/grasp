# -*- coding: UTF-8 -*-
import re


title_re = re.compile(r'<title>([^\W\d_]+)</title>',re.UNICODE)

word_specs_re = re.compile(r'==\s?\{\{([^\W\d_]+)\|([^\W\d_]+)\}\}\s?==',re.UNICODE)

word_replace1_re = re.compile(r'\{\{plm\|([^\W\d_]+)\}\}')

word_replace2_re = re.compile(r'\[\[\s?([^\W\d_]+)\s?\]\]')

number_replace_re = re.compile(r';(\d+):')

clear_re = re.compile(r'\{\{\s?clear\s?\}\}')



def find_title(data) :
    m = title_re.search(data)
    if m :
	return m.group(1)
    else :
	return None
    
    
def find_word_specs(data) :
    m = word_specs_re.search(data)
    if m :
	return [m.group(1),m.group(2)]
    else :
	return None
    
def word_replace1(data) :
    m = word_replace1_re.sub(r'\1',data)
    if m :
	return m
    else :
	return None    

def word_replace2(data) :
    m = word_replace2_re.sub(r'\1',data)
    if m :
	return m
    else :
	return None

def number_replace(data) :
    m = number_replace_re.sub(r'\1',data)
    if m :
	return m
    else :
	return None

def remove_clear(data) :
    m = clear_re.sub(r'',data)
    if m :
	return m
    else :
	return None
    

#def findWordSpecs(data) :
    #p = re.compile(r'==([a-zA-Z0-9ñÑ]+)==',re.UNICODE)
    #m = p.match(word)
    #if m :
	#return m.group(1)
    #else
	#return ''
    
    
#def cleanContents(data) :
    




