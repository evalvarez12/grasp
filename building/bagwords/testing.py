import tree as tr
import extract as ext
import db as db


words=ext.processFile("test_data.txt")

t=tr.Tree()
for i in words :
    if len(i)>3 :
        t.insert_word(i)
    
    
db.dump(t,'test.db')