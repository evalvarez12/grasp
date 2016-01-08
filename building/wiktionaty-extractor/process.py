import regs as regs
import sub_text as subs










CORPUS = 'samples.txt'
INDEX_LINES = 'samples-index.txt'


indexes = subs.get_lines(INDEX_LINES,CORPUS)

with open(CORPUS,'r') as corpus :
    corpus = corpus.readlines()
    for index in indexes :
	sub_text = ''.join(corpus[index[0]-1:index[1]-1])
	sub_text = unicode(sub_text, "utf-8")
	#Double check if title is correct	
	title = regs.find_title(sub_text)
	if title != index[2] :
	    print "ERROR EN  TITULOS"
	    #raise title_exeption()
	    
	
	
	
	
	
	    
 

	