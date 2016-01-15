import re 

class Words :
    
    def __init__(self) :
	number_replace_re = re.compile(r';(\d+)\s?(\{\{([^\W\d_]+)\}\})?:',re.UNICODE)

	self.word_replace2_re = re.compile(r'\[\[\s?([a-zA-ZñÑáéíóú\s|]+)\s?\]\]',re.UNICODE) 
 
	self.ignore1_re = re.compile(r'\[(.*?)\]',re.UNICODE)

	self.ignore2_re = re.compile(r'\&quot;(.*?)\&quot;',re.UNICODE)

	self.ignore3_re = re.compile(r'\&lt;(.*?)\&gt;',re.UNICODE)

ejemplo_re = re.compile(r":\*'''([^']+)'''",re.UNICODE)

dots_remove_re = re.compile(r"::",re.UNICODE)

special_info_re = re.compile(r'\{\{\s?(.*?)\s?\}\}',re.UNICODE)

#special_info_re = re.compile(r'\{\{\s?([^\W\d_]+)(?=(\|[[^\W\d_]+])|(\s?\}\}))',re.UNICODE)

verbal_form_re = re.compile(ur'={2,4}\s?([Ff]orma\s?[a-zA-ZñÑáéíóú\s]+)\s?={2,4}',re.UNICODE)

clear_re = re.compile(r'\{\{\s?clear\s?\}\}')

plm_replace_re = re.compile(r'\{\{plm\|([^\W\d_]+)\}\}',re.UNICODE)

micro_re = re.compile(r'([^\W_]+)=([^\W_]+)',re.UNICODE)