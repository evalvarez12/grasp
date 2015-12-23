import os

rootDir = '.'

for dirname, subdirList, fileList in os.walk(rootDir) :
    print 'Found directory: ',dirname
    for fname in fileList :
	print fname