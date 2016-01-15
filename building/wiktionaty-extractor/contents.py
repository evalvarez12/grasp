import re

class Contents :
    def __init__(self) :
	separator1_re = re.compile(ur'={2,4}\s?\{\{[a-zA-ZñÑáéíóú\s]+\|[a-zA-ZñÑáéíóú\s]+\}\}\s?={2,3}(.*?)(?===)',re.UNICODE | re.DOTALL)
	
	separator2_re = re.compile(ur'={2,4}\s?[Ff]orma\s?[a-zA-ZñÑáéíóú\s]+\s?={2,3}(.*?)(?===)',re.UNICODE | re.DOTALL)
	
    def get_contents_form(data) :
	m = separator2_re.search(data)
	if m :
	    return m.group(1)
	else :
	    return None
	
    def get_contents_regular(data) :
	matches = separator1_re.finditer(data)
	return [match.group(1) for match in matches]