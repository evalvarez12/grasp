import procs.contents as conts
import procs.words as words
import subtext as subs
import procs.formt as formt
import sqlite3 as lite
import re


WordsProc = words.Words()
ContsProc = conts.Contents()
FormatProc = formt.Format()


CORPUS = 'samples.txt'
INDEX_LINES = 'samples-index.txt'

DB_NAME = 'source.db'

indexes = subs.get_lines(ContsProc,INDEX_LINES,CORPUS)
con = lite.connect(DB_NAME)
with con :
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dic(word TEXT, def INT)")
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
	    
	    #print title
	    try :
		contents = subs.get_contents(ContsProc,WordsProc,FormatProc,sub_text)
		s='INSERT INTO dic VALUES(' + '"' + title + '"'  + ',"' + contents + '")'
		cur.execute(s)
	    except :
		print "ERROR ON TITLE: ",title
		
	    
	    
	    #contents = '--' + title + '--\n' + contents
	    #print contents
		
	    
	    
	
	
	
	    
 

	