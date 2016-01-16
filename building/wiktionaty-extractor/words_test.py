# -*- coding: UTF-8 -*-
import words as words
import unittest

WordsProc = words.Words()

class TestExtract(unittest.TestCase) :
    def test1(self) :
	self.assertEqual(WordsProc.solve_keys(u" {{gentilicio2|[[Alemania]]}}.   {{plm|alemán}}  {{inflect.es.adj.agudo-cons|catal|á|n}}"),u" ")

    def test2(self) :
	self.assertEqual(WordsProc.solve_squares(u" [[germánico|germánica]] [[occidental]]  [[w:algo|esto si]]"),u" ")

    #def test1(self) :
	#self.assertEqual(WordsProc.clean_contents(u":*'''Ejemplos:''' como [[ palabra ]] aquí [http link]"),u"Ejemplos: como palabra  aquí ")

    #def test4(self) :
	#self.assertEqual(WordsProc.clean_contents("::''Correr'' tras un ascenso. &lt;small&gt;"),"''Correr'' tras un ascenso. ")

    #def test5(self) :
	#self.assertEqual(WordsProc.clean_contents(" ;1: ;2:")," 1 2")
	
    #def test6(self) :
	#self.assertEqual(WordsProc.clean_contents(r" ;1 {{Tema}}: Este tema es ... {{sinonimos|un sinonimo}}{{ clear }}")," 1 Tema: Este tema es ... sinonimos un sinonimo")	
	
    #def test7(self) :
	#self.assertEqual(WordsProc.clean_contents(ur";1: {{forma verbo|translimitar|p=1s|t=futuro|m=subjuntivo|leng=es}}."),ur"1 forma verbo translimitar persona: 1s tiempo: futuro modo: subjuntivo lengua: Español.")		

if __name__ == '__main__':
    unittest.main()

