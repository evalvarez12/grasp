import sqlite3 as lite
import re 
import sys,os
import building.bagwords.db as db
import building.bagwords.extract as ext
import building.bagwords.tree as tree


#The doc name comes as an argument
INPUT_FILE = str(sys.argv[1])
OUTPUT_FILE = url.split('.')[0] + '-output' + url.split('.')[1]
#print '-LOADING DATABASE-'
#t = tree.Tree()
#db.load(t,'source.db')

print '-PROCESSING INPUT TEXT-'
input_words = ext.process_file(file_name)
with open(INPUT_FILE) as input_file, open(OUTPUT_FILE) as output_file :
    input_words = ext.process_text(input_file.read())
    con = lite.connect('source.db')
    with con :
	con.text_factory = str
	cur = con.cursor()
	for i in input_words :
	    word = i.lower()
	    s = "SELECT times from bag where word = '" + word + "'"
	    cur.execute(s)
	    count = cur.fetchone()
	    print count
	    if count :
		if count[0] < 1500 :
		    s = "SELECT def from dic where word = '" + i + "'"
		    cur.execute(s)
		    if cur.fetchone :
			print i,cur.fetchone()[0]
	    
    
