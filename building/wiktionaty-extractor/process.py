import contents as conts
import words as words
import subtext as subs
import re


WordsProc = words.Words()
ContsProc = conts.Contents()


CORPUS = 'samples.txt'
INDEX_LINES = 'samples-index.txt'


indexes = subs.get_lines(ContsProc,INDEX_LINES,CORPUS)

with open(CORPUS,'r') as corpus :
    corpus = corpus.readlines()
    for index in indexes :
	sub_text = ''.join(corpus[index[0]-1:index[1]-1])
	sub_text = unicode(sub_text, "utf-8")
	#Double check if title is correct	
	title = ContsProc.find_title(sub_text)
	if title != index[2] :
	    print "ERROR EN  TITULOS"
	    #raise title_exeption()
	contents = subs.get_contents(ContsProc,WordsProc,sub_text)
	contents = '--' + title + '--\n' + contents
	print contents
	    
	
	
	
	
	
	    
 

	