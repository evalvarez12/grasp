# -*- coding: UTF-8 -*-
import re

#symbols = [",", ".", ";", ":", "'", '"',"`", "(", ")", '/', "&","?", "!","*","<",">","\r","\t"]
#TO DO add space recognition eiter tab or space


words_re = re.compile(r'\b([^\W\d_]+)\b',re.UNICODE) #all character on unicode without digits and such

def process_file(filename) :
    with open(filename, 'r') as data :
        return process_text(data.read())
    #except EnvironmentError : 
        #print "ERROR: Can't load file"
        #return None
  
def process_text(data) :
    lines = data.split("\n")
    processed = []
    for i in lines :
        processed += process_line(i)    
    return processed  
  
def process_line(data) :
    return words_re.findall(data)
    #words = data.split(" ")
    #processed_words = []
    #for i in words :
        #processed_words += processWord(i)    
    #return processed_words



#def processWord(word) :
    #if word.count("-") :
        #extra_words = word.split("-")
        #words = []
        #for i in extra_words :
            #words += processWord(i)
        #return words
    #else :
        #for sym in symbols :
            #word = word.replace(sym,"")
        #if word == "" :
            #return []
        #else :
            #word = word.lower()  
            #if word.isdigit() :
	        #word = "#"  
            #return [word]