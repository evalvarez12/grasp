# -*- coding: UTF-8 -*-
import re


title_re = re.compile(r'<title>([^\W\d_]+)</title>',re.UNICODE)

word_specs_re = re.compile(r'={2,3}\s?\{\{([^\W\d_]+)\|([^\W\d_]+)\}\}\s?={2,3}',re.UNICODE)

word_replace2_re = re.compile(r'\[\[\s?([^\W\d_]+)\s?\]\]',re.UNICODE)

number_replace_re = re.compile(r';(\d+)\s?(\{\{([^\W\d_]+)\}\})?:',re.UNICODE)

separator1_re = re.compile(r'={2,3}\s?\{\{[^\W\d_]+\|[^\W\d_]+\}\}\s?={2,3}([^(===)(==)]*)[=]{2,3}',re.UNICODE)

separator2_re = re.compile(r'={2,3}\s?[Ff]orma\s?[Vv]erbal\s?={2,3}([^(===)(==)]*)[=]{2,3}',re.UNICODE)

ignore1_re = re.compile(r'\[(.*)\]',re.UNICODE)

ignore2_re = re.compile(r'\&quot;(.*)\&quot;',re.UNICODE)

ignore3_re = re.compile(r'\&lt;(.*)\&gt;',re.UNICODE)

ejemplo_re = re.compile(r":\*'''([^']+)'''",re.UNICODE)

dots_remove_re = re.compile(r"::",re.UNICODE)

special_info_re = re.compile(r'\{\{\s?(.*)\s?\}\}',re.UNICODE)

verbal_form_re = re.compile(r'={2,3}\s?[Ff]orma\s?[Vv]erbal\s?={2,3}')

#clear_re = re.compile(r'\{\{\s?clear\s?\}\}') #SOBRA

#word_replace1_re = re.compile(r'\{\{plm\|([^\W\d_]+)\}\}',re.UNICODE)




def find_title(data) :
    m = title_re.search(data)
    if m :
	return m.group(1)
    else :
	return None
    
def find_word_specs(data) :
    specs = word_specs_re.findall(data)
    return specs

    
def resolve_word_specs(data) :
    m = word_specs_re.search(data)
    if m :
	return [m.group(1),m.group(2)]
    else :
	return None
    
    
def get_contents(data) :
    contents = separator2_re.findall(data)
    if contents :
	return contents
    else :
	m2 = separator1_re.search(data)
	if m2 :
	    return m2.group(1)
	else :
	    return None

	
def clear_words(data) :
    data = word_replace2_re.sub(r'\1',data)
    data = ejemplo_re.sub(r'\1',data)
    data = ignore1_re.sub(r'',data)
    data = ignore2_re.sub(r'',data)
    data = ignore3_re.sub(r'',data)
    data = dots_remove_re.sub(r'',data)
    m = number_replace_re.search(data)
    if m :
	if m.group(2) :
	    return number_replace_re.sub(r'\1 \3',data)
	else :
	    return number_replace_re.sub(r'\1',data)
    else :
	return data
	
def special_info(data) :
    m = special_info_re.search(data)
    if m :
	return [m.group(1),m.group(2)]
    else :
	return None


def cases(data) :
    if '.' not in data :
	groups = data.split('|')
	return groups
    else : 
	return []
    
def resolve_type(data) :
    verbal_form_match = verbal_form_re.search(data)
    
    
#def word_replace1(data) :
    #return word_replace1_re.sub(r'\1',data)


#def word_replace2(data) :
    #return word_replace2_re.sub(r'\1',data)


#def number_replace(data) :
    #m = number_replace_re.search(data)
    #if m.group(2) :
	#return number_replace_re.sub(r'\1 \3',data)
    #else :
	#return number_replace_re.sub(r'\1',data)

#def remove_clear(data) :
    #return clear_re.sub(r'',data)
    
    