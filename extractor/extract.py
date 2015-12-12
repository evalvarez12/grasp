
symbols = [",", ".", ";", ":", "'", '"', "(", ")", '/', "&","?", "!"]

def processFile(filename) :
    with open(filename, 'r') as data :
        return process(data.read())
    #except EnvironmentError : 
        #print "ERROR: Can't load file"
        #return None
  
  
  
def process(data) :
    words = data.split(" ")
    processed_words = []
    for i in words :
        processed_words += processWord(i)    
    return processed_words



def processWord(word) :
    if word.count("-") :
        extra_words = word.split("-")
        words = []
        for i in extra_words :
            words += processWord(i)
        return words
    elif word.count("\n") :
        extra_words = word.split("\n")
        words = []
        for i in extra_words :
            words += processWord(i)
        return words
    else :
        for sym in symbols :
            word = word.replace(sym,"")
        if word == "" :
            return []
        else :
            word = word.lower()  
            if word.isdigit() :
	        word = "#"  
            return [word]