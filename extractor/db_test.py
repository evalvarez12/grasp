import db as db
import unittest
import extract as ext
import sqlite3 as lite


text = "Some test text to test the text count in a test text count"


db_name='test.db'






class TestTree(unittest.TestCase) :

    
    def test_insertWord(self) :
	db.createNewTable(db_name)
	processed = ext.process(text)
	for i in processed :
	    db.insertWord(i,db_name)
	compare=[("some",1),("test",3),("text",3),("to",1),("the",1),("count",2),("in",1),("a",1)]    
	
	con=lite.connect(db_name)
	with con  :
	    cur = con.cursor() 
	    cur.execute("SELECT * FROM Counts")
	    a=cur.fetchall()
	    self.assertItemsEqual(a,compare) 
	    


if __name__ == '__main__':
  unittest.main()

      