# -*- coding: UTF-8 -*-
import regs as regs
import subtext as sub
import subprocess
import random

CORPUS = '/home/eduardo/Trabajo/wikidumps/dumps/eswiktionary-20151226-pages-articles-multistream.xml'
INDEX = '/home/eduardo/Trabajo/wikidumps/dumps/wiktionary-line-index.txt'


lines_index = sub.get_lines(INDEX,CORPUS)

command = "rm samples.txt"
subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)

for i in range(10) :
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