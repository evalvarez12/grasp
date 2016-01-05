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
	
    


