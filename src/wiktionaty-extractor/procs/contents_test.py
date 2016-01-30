# -*- coding: UTF-8 -*-
import contents as conts
import unittest

ContProc = conts.Contents()

class TestExtract(unittest.TestCase) :
    
    def test1(self) :
	self.assertEqual(ContProc.find_sections(ur" Precontenido === {{verbo circunstáncial |fr}} === \n primer_contenido \n === {{sustantivo|es}} masculino ===segundo contenido === {{algo|ru}} === TERCERcontenído === FIN ==="),[ur" {{verbo circunstáncial |fr}} ",ur" {{sustantivo|es}} masculino ",ur" {{algo|ru}} ",ur" FIN "])	
	   
    def test2(self) :
	self.assertEqual(ContProc.get_contents(u" Precontenido === {{verbo circunstáncial |fr}} === \n primer_contenido \n=== {{sustantivo|es}} masculino ===segundo contenido === {{algo|ru}} === TERCERcontenído === FIN ===",u" {{verbo circunstáncial |fr}} "),u" \n primer_contenido \n")	
	

if __name__ == '__main__':
    unittest.main()

     