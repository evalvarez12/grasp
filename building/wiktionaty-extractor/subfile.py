import regs as regs
import re as re

def get_contents(data) :
    form_match = regs.get_contents_form(data) 
    contents = ''
    if form_match :
	print "form"
        contents = contents + regs.clean_contents(data) + '\n'
    specs = regs.find_word_specs(data)
    if specs :
	print specs
	regular_contents = regs.get_contents_regular(data)
	for i in range(len(specs)) :
	    contents += specs[i][0] + ' ' + specs[i][1] + '\n'
	    contents += regs.clean_contents(regular_contents[i]) + '\n'
    return contents
       
       
       
#def clean_contents(data) :
    #data = regs.clear_words(data)
    #special = regs.special_info_re.findall(data)
    #for i in special :
	#info = i.split('|')
	#if info[0] == 'clear' :
	    #data = re.sub(r'{{clear}},'r'',data)
	#elif info[0] == 'plm' :
	    #data = re.sub(r'{{}})