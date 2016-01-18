# -*- coding: UTF-8 -*-
import subtext as sub
import procs.contents as conts
import subprocess
import random

CORPUS = '/home/eduardo/Trabajo/wikidumps/dumps/eswiktionary-20151226-pages-articles-multistream.xml'
INDEX_LINES = '/home/eduardo/Trabajo/wikidumps/dumps/wiktionary-line-index.txt'

ContsProc = conts.Contents()
lines_index = sub.get_lines(ContsProc,INDEX_LINES,CORPUS)

command = "rm samples.txt"
subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)

for i in range(50) :
    index = lines_index[i]
    #index = random.choice(lines_index)
    command = "sed -n '" + str(index[0]) + "," + str(index[1]) + "p' " + CORPUS + " >> samples.txt"
    process = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    process.communicate()
    
    separator = 'echo "##########################################################################" >> samples.txt'
    process = subprocess.Popen(separator,stdout=subprocess.PIPE,shell=True)
    process.communicate()
    

#for i in lines_index :
    #if i[2] == u"niño" :
	#j = i
    
#index = j
#command = "sed -n '" + str(index[0]) + "," + str(index[1]) + "p' " + CORPUS + " >> samples.txt"
#process = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
#process.communicate()
    
#separator = 'echo "##########################################################################" >> samples.txt'
#process = subprocess.Popen(separator,stdout=subprocess.PIPE,shell=True)
#process.communicate()    