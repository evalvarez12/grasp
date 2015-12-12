import sqlite3 as lite
import sys



def create_table_counts(db_name) :
    con=lite.connect(db_name)
    with con  :
        cur = con.cursor() 
        cur.execute("CREATE TABLE IF NOT EXISTS Counts(word TEXT, times INT)")


    
def insert(word,db_name) :
    con=lite.connect(db_name)
    with con  :
        cur = con.cursor() 
        cur.execute("SELECT * FROM Counts WHERE word = ?",(word,))
        data=cur.fetchone()
        if data is None :
            cur.execute("INSERT INTO Counts VALUES(" + "'" + str(1) + "'"  + "," + word + ")")
        else :
	    cur.execute("UPDATE Counts SET times = times + 1 WHERE word =" + word)
	    