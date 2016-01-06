# -*- coding: UTF-8 -*-
import re


title_re = re.compile(r'<title>([^\W\d_]+)</title>',re.UNICODE)

word_specs_re = re.compile(r'==\s?\{\{([^\W\d_]+)\|([^\W\d_]+)\}\}\s?==',re.UNICODE)

word_replace1_re = re.compile(r'\{\{plm\|([^\W\d_]+)\}\}')

word_replace2_re = re.compile(r'\[\[\s?([^\W\d_]+)\s?\]\]')

number_replace_re = re.compile(r';(\d+)\s?(\{\{([^\W\d_]+)\}\})?:') #FIX THIS

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
    return word_replace1_re.sub(r'\1',data)


def word_replace2(data) :
    return word_replace2_re.sub(r'\1',data)


def number_replace(data) :
    m = number_replace_re.search(data)
    if m.group(2) :
	return number_replace_re.sub(r'\1 \3',data)
    else :
	return number_replace_re.sub(r'\1',data)

def remove_clear(data) :
    return clear_re.sub(r'',data)

    





