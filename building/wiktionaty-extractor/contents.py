# -*- coding: UTF-8 -*-
import re
import spanish.lang as lang

class Contents :
    def __init__(self) :
	self.separator1_re = re.compile(ur'={2,4}\s?\{\{[\w\s]+\|[\w\s]+\}\}\s?={2,3}(.*?)(?===)',re.UNICODE | re.DOTALL)
	self.separator2_re = re.compile(ur'={2,4}\s?[Ff]orma\s?[\w\s]+\s?={2,3}(.*?)(?===)',re.UNICODE | re.DOTALL)
	self.title_re = re.compile(r'<title>([^\W\d_]+)</title>',re.UNICODE)
	self.word_specs_re = re.compile(ur'={2,4}\s?\{\{([\w\s]+)\|([\w\s]+)\}\}\s?={2,4}',re.UNICODE)  #FIND A MORE CIVILIZED WAY TO DO THIS

    def get_contents_form(self,data) :
	m = self.separator2_re.search(data)
	if m :
	    return m.group(1)
	else :
	    return None
	
    def get_contents_regular(self,data) :
	matches = self.separator1_re.finditer(data)
	return [match.group(1) for match in matches]
    
    def find_title(self,data) :
	m = self.title_re.search(data)
	if m :
	    return m.group(1)
	else :
	    return None
	
    def find_word_specs(self,data) :
	specs = self.word_specs_re.findall(data)
	new_specs = []
	for i in specs :
	    try :
		new_specs += [(i[0],lang.LANGUAGES[i[1]])]
	    except KeyError :
		new_specs += [(i[0],'lengua desconocida')]
	return new_specs

	
    def resolve_word_specs(self,data) :
	m = self.word_specs_re.search(data)
	if m :
	    return [m.group(1),m.group(2)]
	else :
	    return None
	