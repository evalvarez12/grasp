# -*- coding: UTF-8 -*-
import db as db
import unittest
import extract as ext
import sqlite3 as lite
import tree as tr


text = u"Una prueba con palabras con ácentos y demas ñoñerias"


db_name='test.db'






class TestDB(unittest.TestCase) :

    
    def test_insertWord(self) :
	db.createNewTable(db_name)
	processed = ext.process_line(text)
	for i in processed :
	    db.insertWord(i,db_name)
	compare=[(u"Una",1),(u"prueba",1),(u"palabras",1),(u"con",2),(u"ácentos",1),(u"y",1),(u"demas",1),(u"ñoñerias",1)]    
	
	con=lite.connect(db_name)
	with con  :
	    cur = con.cursor() 
	    cur.execute("SELECT * FROM bag")
	    a=cur.fetchall()
	    self.assertItemsEqual(a,compare) 
	    

t=tr.Tree()
list_words =[u"prueba",u"niño",u"árbol",u"día",u"gato",u"perro"]
for i in list_words :
    t.insert_word(i)

t.insert_word(u"día",4)
t.insert_word(u"árbol",1)



class TestTreeDB(unittest.TestCase) :
    #def test_create_tree(self) :
    #self.failUnlessRaises(ValueError,tr.Tree)
      
  def test_dump_load(self) :
    db.dump(t,'test.db')
    t2=tr.Tree()
    db.load(t2,'test.db')
    a=t.traverse('')
    b=t2.traverse('')
    #print a,b
    #b = [unicode(i,'utf-8') for i in b]
    self.assertItemsEqual(a,b) 
    


if __name__ == '__main__':
    unittest.main()

      