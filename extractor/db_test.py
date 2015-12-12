import db as db
import unittest


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

      