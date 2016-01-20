import sqlite3 as lite
import sys
import tree as tr
#Table used to words and keep record of appearances
#TABLE bag(word TEXT, times INT)


def useTable(db_name) :
    con=lite.connect(db_name)
    with con  :
        cur = con.cursor() 
        cur.execute("CREATE TABLE IF NOT EXISTS bag(word TEXT, times INT)")
        
def createNewTable(db_name) :
    con=lite.connect(db_name)
    with con  :
        cur = con.cursor()
        cur.execute("DROP TABLE if exists bag")
        cur.execute("CREATE TABLE bag(word TEXT, times INT)")        

    
def insertWord(word,db_name) :
    con=lite.connect(db_name)
    with con  :
        cur = con.cursor() 
        cur.execute("SELECT rowid FROM bag WHERE word = '" + word + "'")
        data=cur.fetchone()
        if data :
	    cur.execute("UPDATE bag SET times = times + 1 WHERE rowid = " + str(data[0]))
        else :
	    cur.execute("INSERT INTO bag VALUES(" + "'" + word + "'"  + ",1)")
	   
	   
	   
def dump(t,db_name) :
    con=lite.connect(db_name)
    with con  :
	con.text_factory = str
	cur = con.cursor() 
	a=t.traverse('')
	cur.execute("DROP TABLE if exists bag")
	cur.execute("CREATE TABLE bag(word TEXT, times INT)")
	for k,v in a.iteritems() :
	    s="INSERT INTO bag VALUES(" + "'" + k + "'"  + "," + str(v) + ")"
	    cur.execute(s)


def load(t,db_name) :
    con=lite.connect(db_name)
    with con :
	con.text_factory = str
	cur = con.cursor() 
	s="SELECT * FROM bag"
	cur.execute(s)
	items = cur.fetchall()
	for i in items :
	    t.insert_word(str(i[0]),i[1])
    	   