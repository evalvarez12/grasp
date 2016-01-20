import db as db
import unittest
import extract as ext
import sqlite3 as lite
import tree as tr


text = "Some test text to test the text count in a test text count"


db_name='test.db'






class TestDB(unittest.TestCase) :

    
    def test_insertWord(self) :
	db.createNewTable(db_name)
	processed = ext.process_line(text)
	for i in processed :
	    db.insertWord(i,db_name)
	compare=[("Some",1),("test",3),("text",3),("to",1),("the",1),("count",2),("in",1),("a",1)]    
	
	con=lite.connect(db_name)
	with con  :
	    cur = con.cursor() 
	    cur.execute("SELECT * FROM bag")
	    a=cur.fetchall()
	    self.assertItemsEqual(a,compare) 
	    

t=tr.Tree()
list_words =["test","command","cat","caterpillar","chown","chmod","chroot","table","word","words"]
for i in list_words :
    t.insert_word(i)

t.insert_word("words",4)
t.insert_word("word",1)



class TestTree(unittest.TestCase) :
    #def test_create_tree(self) :
    #self.failUnlessRaises(ValueError,tr.Tree)
      
  def test_dump_load(self) :
    db.dump(t,'test.db')
    t2=tr.Tree()
    db.load(t2,'test.db')
    a=t.traverse('')
    b=t2.traverse('')
    self.assertItemsEqual(a,b) 
    


if __name__ == '__main__':
    unittest.main()

      