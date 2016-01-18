import os
import building.extractor.extract as ext
import building.extractor.db as db
import building.extractor.tree as tr



rootDir = '/home/bruno/Eduardo/text/'
#rootDir = '/home/eduardo/Trabajo/text/'


t=tr.Tree()

for dirname, subdirList, fileList in os.walk(rootDir) :
    print 'Working in directory: ',dirname
    for fname in fileList :
	print 'Processing file: ',fname
	complete_fname =  dirname + '/' + fname
	words=ext.processFile(complete_fname)
	
	
	for i in words :
            if len(i)>3 :
		try :
                    t.insert_word(i)
                except :
		    print "TREE ERROR ON WORD: ",i
		    print "FILE: ",complete_fname
	
db.dump(t,'train.db')