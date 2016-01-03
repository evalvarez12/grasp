




def modeSelector(line,mode) :
    if mode == 'FindTitle' :
	findTitle(line)
    elif mode == 'getWordSpecs' :
	findWordSpecs(line)
    else :
	cleanContents(line)
    
