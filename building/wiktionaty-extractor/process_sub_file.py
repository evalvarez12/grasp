import regs as regs
import re as re

def get_contents(data) :
   contents = regs.get_content_verbal(data) 
   if contents :
       return clean_contents(data)
   else :
       contents = regs.get_content_regular(data)
       return clean_contents(data)
       
       
       
def clean_contents(data) :
    data = regs.clear_words(data)
    special = regs.special_info_re.findall(data)
    for i in special :
	info = i.split('|')
	if info[0] == 'clear' :
	    data = re.sub(r'{{clear}},'r'',data)
	elif info[0] == 'plm' :
	    data = re.sub(r'{{}})