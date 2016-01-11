# -*- coding: UTF-8 -*-
import re
import spanish.lang as lang

#a=r'[=]{2,3}\s?[a-zA-Z\{\}\|]+\s?[=]{2,3}'


title_re = re.compile(r'<title>([^\W\d_]+)</title>',re.UNICODE)

word_specs_re = re.compile(ur'={2,4}\s?\{\{([a-zA-ZñÑáéíóú\s]+)\|([a-zA-ZñÑáéíóú\s]+)\}\}\s?={2,4}',re.UNICODE)  #FIND A MORE CIVILIZED WAY TO DO THIS

word_replace2_re = re.compile(r'\[\[\s?([^\W\d_]+)\s?\]\]',re.UNICODE)

number_replace_re = re.compile(r';(\d+)\s?(\{\{([^\W\d_]+)\}\})?:',re.UNICODE)

separator1_re = re.compile(ur'={2,4}\s?\{\{[a-zA-ZñÑáéíóú\s]+\|[a-zA-ZñÑáéíóú\s]+\}\}\s?={2,3}([^(===)(==)]*)(?=[=]{2,4})',re.UNICODE)

separator2_re = re.compile(ur'={2,4}\s?[Ff]orma\s?[a-zA-ZñÑáéíóú\s]+\s?={2,3}([^(===)(==)]*)(?=[=]{2,4})',re.UNICODE)

ignore1_re = re.compile(r'\[(.*)\]',re.UNICODE)

ignore2_re = re.compile(r'\&quot;(.*)\&quot;',re.UNICODE)

ignore3_re = re.compile(r'\&lt;(.*)\&gt;',re.UNICODE)

ejemplo_re = re.compile(r":\*'''([^']+)'''",re.UNICODE)

dots_remove_re = re.compile(r"::",re.UNICODE)

special_info_re = re.compile(r'\{\{\s?(.*)\s?\}\}',re.UNICODE)

#special_info_re = re.compile(r'\{\{\s?([^\W\d_]+)(?=(\|[[^\W\d_]+])|(\s?\}\}))',re.UNICODE)

verbal_form_re = re.compile(ur'={2,4}\s?([Ff]orma\s?[a-zA-ZñÑáéíóú\s]+)\s?={2,4}',re.UNICODE)

clear_re = re.compile(r'\{\{\s?clear\s?\}\}')

plm_replace_re = re.compile(r'\{\{plm\|([^\W\d_]+)\}\}',re.UNICODE)

micro_re = re.compile(r'([^\W\d_]+)=([^\W\d_]+)',re.UNICODE)


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
    
    
def get_contents_form(data) :
    m = separator2_re.search(data)
    if m :
	return m.group(1)
    else :
	return None

    
def get_contents_regular(data) :
    matches = separator1_re.finditer(data)
    return [match.group(1) for match in matches]

	
def clean_contents(data) :
    data = word_replace2_re.sub(r'\1',data)
    data = ejemplo_re.sub(r'\1',data)
    data = ignore1_re.sub(r'',data)
    data = ignore2_re.sub(r'',data)
    data = ignore3_re.sub(r'',data)
    data = dots_remove_re.sub(r'',data)
    data = clear_re.sub(r'',data)
    data = plm_replace_re.sub(r'\1',data)
    
    m = number_replace_re.search(data)
    if m :
	if m.group(2) :
	    data = number_replace_re.sub(r'\1 \3:',data)
	else :
	    data = number_replace_re.sub(r'\1',data)
	    
    data = special_info(data)
    
    return data

	
def special_info(data) :
    info = special_info_re.findall(data)
    cleaned = []
    for i in info :
	to_join = []
	info_groups = i.split('|')
	for j in info_groups :
	    to_join += microprocess(j)
	cleaned += [" ".join(to_join)]
    
    for i in range(len(info)) :
	to_replace = r"{{" + info[i] + r"}}"
	data = data.replace(to_replace,cleaned[i])
	
    return data


def microprocess(data) :
    m = micro_re.search(data)
    if m :
	if m.group(1) == ('leng' or 'lengua') :
	    return [u"Lengua: " + unicode(lang.LANGUAGES[m.group(2)],"utf-8")]
	else :
	    return [" ".join([m.group(1),m.group(2)])]
    elif 'forma' in data :
	return [data] 
    else :
	return [data]
    
	

#def cases(data) :
    #if '.' not in data :
	#groups = data.split('|')
	#return groups
    #else : 

    
    
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
    
    