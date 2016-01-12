import regs as regs
import re as re

def get_contents(data) :
    form = regs.get_contents_form(data) 
    contents = ''
    if form :
        contents = contents + regs.clean_contents(form) + '\n'
    specs = regs.find_word_specs(data)
    if specs :

	regular_contents = regs.get_contents_regular(data)
	for i in range(len(specs)) :
	    contents += specs[i][0] + ' ' + specs[i][1] + '\n'
	    contents += regs.clean_contents(regular_contents[i]) 
    contents = re.sub(' {2}',' ',contents)
    contents = re.sub('\n{2}','\n',contents)
    contents = re.sub('^[ \n]+','',contents)
    contents = re.sub('\n ','\n',contents)
    contents = re.sub('$[ \n]+','',contents)
    return contents
       
       
       
