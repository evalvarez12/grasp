# -*- coding: UTF-8 -*-
import re
import spanish.lang as lang

class Contents :
    def __init__(self) :
	self.sections_re = re.compile(r'={2,4}(.*?)={2,4}',re.UNICODE)
	self.contents_forma_re = re.compile(ur'={2,4}\s?[Ff]orma\s?[\w\s]+\s?={2,4}(.*?)(?===)',re.UNICODE | re.DOTALL)

    def find_sections(self,data) :
	secs = self.sections_re.findall(data)
	return secs
	#return [self.extract_words(i) for i in secs]
	

    def get_contents(self,data,content_title) :
	separator = '={2,4}' + content_title + '={2,4}(.*?)(?===)'
	content = re.search(separator,data,re.UNICODE | re.DOTALL)
	if content :
	    return content.group(1)
	else :
	    return None