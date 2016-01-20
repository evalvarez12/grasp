import os
import building.bagwords.extract as ext
import building.bagwords.db as db
import building.bagwords.tree as tr



#rootDir = '/home/bruno/Eduardo/text/'
rootDir = '/home/eduardo/Trabajo/wikidumps/wikipedia-extractor/text/'


t=tr.Tree()

for dirname, subdirList, fileList in os.walk(rootDir) :
    print 'Working in directory: ',dirname
    for fname in fileList :
	#print 'Processing file: ',fname
	complete_fname =  dirname + '/' + fname
	words=ext.process_file(complete_fname)
	
	
	for i in words :
	    try :
		t.insert_word(i.lower())
            except :
		print "TREE ERROR ON WORD: ",i
		print "FILE: ",complete_fname
	
db.dump(t,'source.db')