# -*- coding: UTF-8 -*-
import contents as conts
import unittest

ContProc = conts.Contents()

class TestExtract(unittest.TestCase) :
    
    def test1(self) :
	self.assertEqual(ContProc.get_contents_regular(ur" Precontenido === {{verbo|fr}} === \n primer_contenido \n === {{sustantivo|es}} ===segundo contenido === {{algo|ru}} === TERCERcontenído === FIN ==="),[ur" \n primer_contenido \n ",ur"segundo contenido ",ur" TERCERcontenído "])	
	
    def test2(self) :
	self.assertEqual(ContProc.get_contents_form(ur" Precontenido === Forma verbal y algo ===  {{forma verbo|reguilar|p=3p|t=pret ind|mindicativo|nopron|leng=es}}.   === {{sustantivo|es}} ==="),ur"  {{forma verbo|reguilar|p=3p|t=pret ind|mindicativo|nopron|leng=es}}.   ")

    def test3(self) :
	self.assertEqual(ContProc.find_title(u"<title>aléman</title>"),u"aléman")

    def test4(self) :
	self.assertEqual(ContProc.find_word_specs(ur"=== {{verbo transitívo|fr}} ===  algun contenido === {{sustantivo|es}} ==="),[(u"verbo transitívo",u"Francés"),(u"sustantivo",u"Español")])
	

if __name__ == '__main__':
    unittest.main()

     