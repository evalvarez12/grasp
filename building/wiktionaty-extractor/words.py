# -*- coding: UTF-8 -*-
import re
import spanish.lang as lang

class Words :
    
    def __init__(self) :
	self.words_re = re.compile(r'\b(\w+)\b',re.UNICODE)
	self.squares_re = re.compile(r'\[\[.*?\]\]',re.UNICODE)
	self.keys_re = re.compile(r'\{\{.*?\}\}',re.UNICODE)
	self.single_squares_re = re.compile(r'\[.*?\]',re.UNICODE)
	self.apos_re = re.compile(r":\*'''([^']+?)'''",re.UNICODE)
	self.quot_re = re.compile(r'\&quot;(.*?)\&quot;',re.UNICODE)
	self.lgt_re = re.compile(r'\&lt;(.*?)\&gt;',re.UNICODE)
	self.micro_re = re.compile(r'([\w]+)=([\w]+)',re.UNICODE)
	self.clear_keys_re = re.compile(r'[\{\}]+')
	self.clear_squares_re = re.compile(r'[\[\]]+')
	
	
	
    def extract_words(self,data) :
	words = self.words_re.findall(data)
	return words
    
    def solve_keys(self,data) :
	keys = self.keys_re.findall(data)
	new_data = data
	for i in keys :
	    pipe_check = i.split('|')
	    if '.' in pipe_check[0] :
		replacement = ''
	    else :
		words = self.extract_words(i)
		# ALL SPECIAL KNOWN CASES
		if words[0] == 'clear' :
		    replacement = ''
		elif words[0] == 'plm' :
		    replacement = ' '.join(words[1:])
		else :
		    replacement = ' '.join(words)
		
	    new_data = new_data.replace(i,replacement)
	return new_data
	    
    def solve_keys_forma(self,data) :
	keys = self.keys_re.findall(data)
	new_data = data
	for i in keys :
	    to_join = []
	    ci = self.clear_keys_re.sub(r'',i)
	    groups = ci.split('|')
	    for j in groups :
		to_join += self.microprocess_forma(j)
		
	    replacement = " ".join(to_join)
	    new_data = new_data.replace(i,replacement)
	return new_data
    
    def microprocess_forma(self,data) :
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
	    
		
    def solve_squares(self,data) :
	squares = self.squares_re.findall(data)
	new_data = data
	for i in squares :
	    ci = self.clear_squares_re.sub(r'',i)
	    words = ci.split('|')
	    # ALL SPECIAL KNOWN CASES
	    if 'w:' in words[0] :
		replacement = ' '.join(words[1:])
	    elif len(words) > 1 :
		replacement = words[0] + "(" + ' '.join(words[1:]) + ")"  
	    else :
		replacement = ' '.join(words)
		
	    #print i,replacement
	    new_data = new_data.replace(i,replacement)
	return new_data
    
    def clean_contents(self,data) :
	new_data = self.solve_keys(data)
	new_data = self.solve_squares(new_data)
	new_data = self.single_squares_re.sub(r'',new_data)
	new_data = self.apos_re.sub(r'\1',new_data)
	new_data = self.quot_re.sub(r'\1',new_data)
	new_data = self.lgt_re.sub(r'',new_data)
	
	return new_data
    
    def clean_contents_form(self,data) :
	new_data = self.solve_keys_forma(data)
	#new_data = self.solve_squares(data)
	#new_data = self.single_squares_re.sub(r'',new_data)
	#new_data = self.apos_re.sub(r'\1',new_data)
	#new_data = self.quot_re.sub(r'\1',new_data)
	#new_data = self.lgt_re.sub(r'',new_data)
	
	
	return new_data
	