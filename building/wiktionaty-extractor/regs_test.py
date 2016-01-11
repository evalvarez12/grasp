# -*- coding: UTF-8 -*-
import regs as regs
import unittest


class TestExtract(unittest.TestCase) :
    
    def test1(self) :
	self.assertEqual(regs.find_title(u"<title>aléman</title>"),u"aléman")

    def test2(self) :
	self.assertEqual(regs.find_word_specs(ur"=== {{verbo transitívo|fr}} ===  algun contenido === {{sustantivo|es}} ==="),[(u"verbo transitívo",u"fr"),(u"sustantivo",u"es")])
	
    def test3(self) :
	self.assertEqual(regs.clean_contents(u":*'''Ejemplos:''' como [[ palabra ]] aquí [http link]"),u"Ejemplos: como palabra aquí ")

    def test4(self) :
	self.assertEqual(regs.clean_contents("::''Correr'' tras un ascenso. &lt;small&gt;"),"''Correr'' tras un ascenso. ")

    def test5(self) :
	self.assertEqual(regs.clean_contents(" ;1: ;2:")," 1 2")
	
    def test6(self) :
	self.assertEqual(regs.clean_contents(r" ;1 {{Tema}}: Este tema es ... {{sinonimos|un sinonimo}}{{ clear }}")," 1 Tema: Este tema es ... sinonimos un sinonimo")	
	
    def test7(self) :
	self.assertEqual(regs.clean_contents(ur";1: {{forma verbo|translimitar|p=1s|t=futuro|m=subjuntivo|leng=es}}."),ur"1 forma verbo translimitar p=1s t futuro m subjuntivo Lengua: Español.")		
	
    def test8(self) :
	self.assertEqual(regs.get_contents_regular(ur" Precontenido === {{verbo|fr}} === \n primer_contenido \n === {{sustantivo|es}} ===segundo contenido === {{algo|ru}} === TERCERcontenído === FIN ==="),[ur" \n primer_contenido \n ",ur"segundo contenido ",ur" TERCERcontenído "])	
	
    def test9(self) :
	self.assertEqual(regs.get_contents_form(ur" Precontenido === Forma verbal y algo ===  {{forma verbo|reguilar|p=3p|t=pret ind|mindicativo|nopron|leng=es}}.   === {{sustantivo|es}} ==="),ur"  {{fomrma verbal|verbo|tiempo|persona}}.   ")


if __name__ == '__main__':
    unittest.main()

      #=== forma verbal y algo === \n ;1: {{forma verbo|reguilar|p=3p|t=pret ind|m=indicativo|nopron=|leng=es}}. === {{verbo intransitivo|es}} ===