# -*- coding: UTF-8 -*-
import sqlite3 as lite
import sys
import fetch as fet
import tools.decode as dec





def build_synonims(db_name) :
    con=lite.connect(db_name)
    with con :
	cur = con.cursor()

	cur.execute("SELECT * FROM depurated")
	items = cur.fetchall()
	
	cur.execute("CREATE TABLE IF NOT EXISTS synonims(word TEXT, syns TEXT)")

    
	for i in items :
	    try :
		word = dec.remove_accents(i[0])
		synonims = fet.getSynonims(word)
		joined = " ".join(synonims)
		
		s="INSERT INTO synonims VALUES('" + i[0] + "','" + joined + "')"
		cur.execute(s)
		
		print 'DONE : ',i[0],joined
	    except :
		print 'ERROR ON : ', i[0]
	    
	    
	    
build_synonims('less-100.db')