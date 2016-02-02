import procs.contents as conts
import procs.words as words
import subtext as subs
import procs.formt as formt
import sqlite3 as lite
import re


WordsProc = words.Words()
ContsProc = conts.Contents()
FormatProc = formt.Format()


CORPUS = '/home/eduardo/Trabajo/wikidumps/dumps/eswiktionary-20151226-pages-articles-multistream.xml'
INDEX_LINES = '/home/eduardo/Trabajo/wikidumps/dumps/wiktionary-line-index.txt'



DB_NAME = '/home/eduardo/Trabajo/grasp/src/source.db'

indexes = subs.get_lines(ContsProc,INDEX_LINES,CORPUS)
con = lite.connect(DB_NAME)
with con :
    con.text_factory = str
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
		print "Mismatch on titles: ",title
		pass

	    #  TO CATCH LAST REBELS - SO FAR NOT NEDEED
	    try :
		contents = subs.get_contents(ContsProc,WordsProc,FormatProc,sub_text)
		if contents :
		    s='INSERT INTO dic VALUES(' + '"' + title + '"'  + ',"' + contents + '")'
		    cur.execute(s)
	    except :
		print "Error processing word: ",title
		# 119 Error on last review
