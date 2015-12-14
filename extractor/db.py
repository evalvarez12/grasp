import sqlite3 as lite
import sys

#Table used to words and keep record of appearances
#TABLE counts(word TEXT, times INT)


def useTable(db_name) :
    con=lite.connect(db_name)
    with con  :
        cur = con.cursor() 
        cur.execute("CREATE TABLE IF NOT EXISTS counts(word TEXT, times INT)")
        
def createNewTable(db_name) :
    con=lite.connect(db_name)
    with con  :
        cur = con.cursor()
        cur.execute("DROP TABLE if exists counts")
        cur.execute("CREATE TABLE Counts(word TEXT, times INT)")        

    
def insertWord(word,db_name) :
    con=lite.connect(db_name)
    with con  :
        cur = con.cursor() 
        cur.execute("SELECT rowid FROM counts WHERE word = '" + word + "'")
        data=cur.fetchone()
        if data :
	    cur.execute("UPDATE Counts SET times = times + 1 WHERE rowid = " + str(data[0]))
        else :
	    cur.execute("INSERT INTO Counts VALUES(" + "'" + word + "'"  + ",1)")
	    