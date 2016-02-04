# -*- coding: UTF-8 -*-
import sqlite3 as lite
import sys

#sys.setdefaultencoding('utf8')



alphabet = [u'a',u'b',u'c',u'd',u'e',u'f',u'g',u'h',u'i',u'j',u'k',u'l',u'm',u'n',u'o',u'p',u'q',u'r',u's',u't',u'u',u'v',u'w',u'x',u'z',u'ñ',u'á',u'é',u'ó',u'í',u'ú']



def discriminate(db_name) :
    con=lite.connect(db_name)
    with con :
	cur = con.cursor()
	s = "SELECT * FROM counts"
	cur.execute(s)
	items = cur.fetchall()
    
	depurated = []
    
	for i in items :
	    flag = 1
	    for j in i[0] :
		if j not in alphabet :
		    flag = 0

	    if flag :
		depurated += [i]
		
	cur.execute("DROP TABLE if exists depurated")	
	cur.execute("CREATE TABLE depurated(word TEXT, times INT)")
	for d in depurated :
	    s="INSERT INTO depurated VALUES(" + "'" + d[0] + "'"  + "," + str(d[1]) + ")"
	    cur.execute(s)
	    
	    
discriminate('train.db')