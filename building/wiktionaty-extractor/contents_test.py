# -*- coding: UTF-8 -*-
import contents2 as conts
import unittest

ContProc = conts.Contents()

class TestExtract(unittest.TestCase) :
    
    def test1(self) :
	self.assertEqual(ContProc.find_sections(ur" Precontenido === {{verbo circunstáncial |fr}} === \n primer_contenido \n === {{sustantivo|es}} masculino ===segundo contenido === {{algo|ru}} === TERCERcontenído === FIN ==="),[ur" \n primer_contenido \n ",ur"segundo contenido ",ur" TERCERcontenído "])	
	   
    def test2(self) :
	self.assertEqual(ContProc.get_contents(ur" Precontenido === {{verbo circunstáncial |fr}} === \n primer_contenido \n === {{sustantivo|es}} masculino ===segundo contenido === {{algo|ru}} === TERCERcontenído === FIN ==="," {{verbo circunstáncial |fr}} "),[ur" \n primer_contenido \n ",ur"segundo contenido ",ur" TERCERcontenído "])	
	

if __name__ == '__main__':
    unittest.main()

     