# -*- coding: UTF-8 -*-
import re
import spanish.lang as lang

class Words :
    
    def __init__(self) :
	self.number_replace_re = re.compile(r';(\d+)\s?(\{\{([\w\[\]\{\}|]+)\}\})?:',re.UNICODE)
	self.word_replace2_re = re.compile(r'\[\[\s?([\w\s|]+)\s?\]\]',re.UNICODE) 
	self.ignore1_re = re.compile(r'\[(.*?)\]',re.UNICODE)
	self.ignore2_re = re.compile(r'\&quot;(.*?)\&quot;',re.UNICODE)
	self.ignore3_re = re.compile(r'\&lt;(.*?)\&gt;',re.UNICODE)
	self.ignore4_re = re.compile(r"^:\*'''\[\[.*?\]\]'''.*$",re.UNICODE)  #REVISAR ESTE RE
	self.ejemplo_re = re.compile(r":\*'''([^']+)'''",re.UNICODE)
	self.dots_remove_re = re.compile(r"::",re.UNICODE)
	self.special_info_re = re.compile(r'\{\{\s?(.*?)\s?\}\}',re.UNICODE)
	#special_info_re = re.compile(r'\{\{\s?([^\W\d_]+)(?=(\|[[^\W\d_]+])|(\s?\}\}))',re.UNICODE)
	self.verbal_form_re = re.compile(ur'={2,4}\s?([Ff]orma\s?[\w\s]+)\s?={2,4}',re.UNICODE)
	self.clear_re = re.compile(r'\{\{\s?clear\s?\}\}')
	self.plm_replace_re = re.compile(r'\{\{plm\|([\w]+)\}\}',re.UNICODE)
	self.micro_re = re.compile(r'([\w]+)=([\w]+)',re.UNICODE)
	
	
    def clean_contents(self,data) :
	data = self.word_replace2_re.sub(r'\1',data)
	data = self.ejemplo_re.sub(r'\1',data)
	data = self.ignore1_re.sub(r'',data)
	data = self.ignore2_re.sub(r'\1',data)
	data = self.ignore3_re.sub(r'',data)
	data = self.ignore4_re.sub(r'',data)
	data = self.dots_remove_re.sub(r'',data)
	data = self.clear_re.sub(r'',data)
	data = self.plm_replace_re.sub(r'\1',data)
	
	m = self.number_replace_re.search(data)
	if m :
	    if m.group(2) :
		data = self.number_replace_re.sub(r'\1 \3:',data)
	    else :
		data = self.number_replace_re.sub(r'\1',data)
		
	data = self.special_info(data)
	
	return data

	    
    def special_info(self,data) :
	info = self.special_info_re.findall(data)
	cleaned = []
	for i in info :
	    to_join = []
	    info_groups = i.split('|')
	    if '.' not in info_groups[0] :	
		for j in info_groups :
		    to_join += self.microprocess(j)
	    cleaned += [" ".join(to_join)]
	
	for i in range(len(info)) :
	    to_replace = r"{{" + info[i] + r"}}"
	    data = data.replace(to_replace,cleaned[i])
	    
	return data


    def microprocess(self,data) :
	m = self.micro_re.search(data)
	if m :
	    if (m.group(1) == 'leng') or (m.group(1) == 'lengua') :
		try :
		    return [u"lengua: " + lang.LANGUAGES[m.group(2)]]
		except KeyError :
		    return [u"lengua: desconocida"]
	    elif m.group(1) == 'p' :
		return [u"persona: " + m.group(2)]
	    elif m.group(1) == 't' :
		return [u"tiempo: " + m.group(2)]
	    elif m.group(1) == 'm' :
		return [u"modo: " + m.group(2)]
	    elif (m.group(1) == u'tít') or (m.group(1) == u'tit') :
		return [m.group(2)]
	    else :
		return [" ".join([m.group(1),m.group(2)])]
	elif 'forma' in data :
	    return [data]
	elif ('=' in data) or ('.' in data) or ('-' in data) :
	    return ['']
	else :
	    return [data]
	