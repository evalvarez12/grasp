# -*- coding: UTF-8 -*-
import re
import spanish.lang as lang

class Contents :
    def __init__(self) :
	self.sections_re = re.compile(r'={2,4}(.*?)={2,4}',re.UNICODE)
	self.contents_forma_re = re.compile(ur'={2,4}\s?[Ff]orma\s?[\w\s]+\s?={2,4}(.*?)(?===)',re.UNICODE | re.DOTALL)
	#self.words_re = re.compile(r'\b(\w+)\b',re.UNICODE)
	self.title_re = re.compile(r'<title>([^\W\d_]+)</title>',re.UNICODE)

    def find_sections(self,data) :
	secs = self.sections_re.findall(data)
	return secs
	#return [self.extract_words(i) for i in secs]
	

    def get_contents(self,data,content_title) :
	content_title = content_title.replace('|','\|')
	content_title = content_title.replace('{','\{')
	content_title = content_title.replace('}','\}')
	reg = '={2,4}' + content_title + '={2,4}(.*?)(?===)'
	#reg =  content_title
	content = re.search(reg,data,re.UNICODE | re.DOTALL)
	if content :
	    return content.group(1)
	else :
	    return ''
	    #reg = '={2,4}' + content_title + '={2,4}(.*?)(?=</text>)'
	    #content = re.search(reg,data,re.UNICODE | re.DOTALL)
	    #if content :
		#return content.group(1)
	    #else :
		#return ''
	
    #def extract_words(self,data) :
	#words = self.words_re.findall(data)
	#return words
    
    def find_title(self,data) :
	m = self.title_re.search(data)
	if m :
	    return m.group(1)
	else :
	    return None