# -*- coding: UTF-8 -*-
import subprocess
import re
import regs as regs

def get_lines(index_file,corpus) :
    number_re = re.compile('\d+')
    marks = []
    with open(index_file) as f :
	for line in f :
	    line_unicode = unicode(line, "utf-8")
	    number_match = number_re.search(line_unicode)
	    title = regs.find_title(line_unicode)
	    marks += [(int(number_match.group()),title)]
	    
    proc = subprocess.Popen(["wc -l " + corpus],stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    m = number_re.search(out)
    marks += [(int(m.group()),'')]
    
    sub_texts = []
    for i in range(len(marks) - 1) :
	start = marks[i][0]
	end = marks[i+1][0] - 1
	title = marks[i][1]
	sub_texts += [(start,end,title)]
	
	
    return sub_texts
	
    



def get_contents(data) :
    form = regs.get_contents_form(data) 
    contents = ''
    if form :
        contents = contents + regs.clean_contents(form) + '\n'
    specs = regs.find_word_specs(data)
    if specs :
	regular_contents = regs.get_contents_regular(data)
	for i in range(len(specs)) :
	    if re.search('[Ll]engua',specs[i][0]) :
		contents = specs[i][0] + ' ' + specs[i][1] + '\n' + contents
	    else :
		contents += specs[i][0] + ' ' + specs[i][1] + '\n'
		contents += regs.clean_contents(regular_contents[i]) 
	    
    contents = re.sub(' {2,}',' ',contents)
    contents = re.sub('\n{2,}','\n',contents)
    contents = re.sub('^[ \n]+','',contents)
    contents = re.sub('\n ','\n',contents)
    contents = re.sub('$[ \n]+','',contents)
    return contents
       
       
       
