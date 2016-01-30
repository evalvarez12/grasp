# -*- coding: UTF-8 -*-
import re
import subprocess
import procs.spanish.lang as lang
import procs.spanish.titles as titles


def get_lines(CProc,index_file,corpus) :
    number_re = re.compile('\d+')
    marks = []
    with open(index_file) as f :
	for line in f :
	    line_unicode = unicode(line, "utf-8")
	    number_match = number_re.search(line_unicode)
	    title = CProc.find_title(line_unicode)
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
	


def get_contents(CProc,WProc,FProc,data) :
    sections = CProc.find_sections(data)
    contents = ''
    for i in sections :
	#print i
	section_words = WProc.extract_words(i)
	if section_words :
	    if (section_words[0] == "Forma") or (section_words[0] == "forma") :
		sec = CProc.get_contents(data,i)
		contents = contents + WProc.clean_contents_form(sec) + '\n'
	    elif section_words[0] in titles.TITLES :
		try :
		    section_words[-1] = lang.LANGUAGES[section_words[-1]]
		except KeyError :
		    try :
			section_words[-2] = lang.LANGUAGES[section_words[-2]]
		    except KeyError :
			pass
		    else :
			contents = contents + ' '.join(section_words) + '\n'
			sec = CProc.get_contents(data,i)
			contents = contents + WProc.clean_contents(sec) + '\n'
		else :
		    contents = contents + ' '.join(section_words) + '\n'
		    sec = CProc.get_contents(data,i)
		    contents = contents + WProc.clean_contents(sec) + '\n'
	    
	    #leng = [len(it) <= 3 for it in section_words]
	    #if leng.count(True) == 1 :
		#ind = leng.index(True)
		#try :
		    #section_words[ind] =  lang.LANGUAGES[section_words[ind]]
		#except KeyError : 
		    #section_words[ind] =  'Lengua desconocida'
		#contents = contents + ' '.join(section_words) + '\n'
		#sec = CProc.get_contents(data,i)

		#contents = contents + WProc.clean_contents(sec) + '\n'

	
    contents = FProc.clean(contents)
    return contents
       

    
       
