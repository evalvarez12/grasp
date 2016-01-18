# -*- coding: UTF-8 -*-
import re
import spanish.lang as lang

class Format :
    def __init__(self) :
	self.double_spaces_re = re.compile(ur'([\s])\1+',re.UNICODE)
	#self.double_newline_re = re.compile(ur'(\n{2,})',re.UNICODE)
        self.start_re = re.compile(ur'^[\W]+',re.UNICODE | re.MULTILINE)
        #self.end_re = re.compile(ur'$[ ]+',re.UNICODE)


    def clean(self,data) :
	#new_data = data
	new_data = self.double_spaces_re.sub(r'\1',data)
	#new_data = self.double_newline_re.sub(r' ',data)
	new_data = self.start_re.sub('',new_data)
	#new_data = self.end_re.sub('',new_data)
	return new_data