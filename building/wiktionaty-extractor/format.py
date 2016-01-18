# -*- coding: UTF-8 -*-
import re
import spanish.lang as lang

class Format :
    def __init__(self) :
	self.double_spaces_re = re.compile('[\s]{2,}')
        self.start_re = re.compile('^[\w]+')
        self.end_re = re.compile('$[\s]+')


    def clean(self,data) :
	new_data = self.double_spaces_re.sub('\1',data)
	new_data = self.start_re.sub('',new_data)
	new_data = self.end_re.sub('',new_data)