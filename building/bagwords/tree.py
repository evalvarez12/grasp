import sys

class Tree(object) :
  def __init__(self) :
    #self.trees = dict(trees) if trees else {}
    self.trees = {}
    self.number = 0
    
  def insert_word(self,word,times=1) :
    if word :
      if word[0] not in self.trees :
        tree1 = Tree()
        self.trees[word[0]] = tree1
        
      try :
        self.trees[word[0]].insert_word(word[1:],times)
      except RuntimeError :
	  print "RECUSION ERROR ON WORD :", word
	  
    else :
      self.number += times

  def word_count(self,word) :
    if word  :
      try :
        return self.trees[word[0]].word_count(word[1:])
      except KeyError :
	print "No word in tree " + word

    else :
      return self.number
      
  def traverse(self,word) :
    if word :
      try :
        return {(word[0]+k):v for k,v in self.trees[word[0]].traverse(word[1:]).iteritems()}
      except : 
        print "Cant tranverse using " + word 
    else :
      l={}
      if self.number != 0  :
	l['']=self.number
      for k,v in self.trees.iteritems() :
	l.update({(k+i):j for i,j in v.traverse(word).iteritems()})

      return l   
    
  def fuzzy(self,word,err) :
    l={}
    if err >= 0 :
      if self.number != 0 and err >= len(word):
	l['']=self.number
      if self.trees :
	if not word : word = ' ' 
        for k,v in self.trees.iteritems() :
	  l.update({(k+i):j for i,j in v.fuzzy(word[1:],err+int(word[0]==k)-1).iteritems()})
    return l

    
   
   
   
   
   
   
   
   
   
   
   
   