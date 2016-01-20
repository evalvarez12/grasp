import sqlite3 as lite
import re 
import sys,os
import building.bagwords.db as db
import building.bagwords.extract as ext
import building.bagwords.tree as tree


#The doc name comes as an argument
file_name = str(sys.argv[1])

#print '-LOADING DATABASE-'
#t = tree.Tree()
#db.load(t,'source.db')

print '-PROCESSING INPUT TEXT-'
input_words = ext.process_file(file_name)

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
	    if count[0] < 100 :
		s = "SELECT def from dic where word = '" + i + "'"
		cur.execute(s)
		if cur.fetchone :
		    print i,cur.fetchone()[0]
	    
    
