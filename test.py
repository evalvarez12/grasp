import sqlite3 as lite
import re 
import sys,os
import string
import codecs
import building.bagwords.db as db
import building.bagwords.extract as ext
import building.bagwords.tree as tree


#The doc name comes as an argument
INPUT_FILE = str(sys.argv[1])
OUTPUT_FILE = INPUT_FILE.split('.')[0] + '-output.' + INPUT_FILE.split('.')[1]
#print '-LOADING DATABASE-'
#t = tree.Tree()
#db.load(t,'source.db')

DEF_TEMPLATE =  string.Template(u'--- $word ---\n$dic\n')

print '-PROCESSING INPUT TEXT-'
#input_words = ext.process_file(file_name)
with open(INPUT_FILE,'r') as input_file, codecs.open(OUTPUT_FILE,'w',"utf-8-sig") as output_file :
    words_defs = ''
    input_text = unicode(input_file.read(),'utf-8')
    input_words = ext.process_text(input_text)
    con = lite.connect('source.db')
    with con :
	con.text_factory = str
	cur = con.cursor()
	for i in input_words :
	    word = i.lower()
	    s = "SELECT times from bag where word = '" + word + "'"
	    cur.execute(s)
	    count = cur.fetchone()
	    #print count
	    if count :
		if count[0] < 1500 :
		    s = "SELECT def from dic where word = '" + i + "'"
		    cur.execute(s)
		    fetch = cur.fetchone()
		    if fetch :
			word_def = unicode(fetch[0],'utf-8')
			input_text = input_text.replace(i,u'[[' + i + u']]')
			#print input_text
			#print repr(i),repr(cur.fetchone()[0])
			words_defs += DEF_TEMPLATE.substitute(word=i,dic=word_def)
			
    
    output_file.write(input_text)
    output_file.write('\n\n')
    output_file.write(words_defs)
