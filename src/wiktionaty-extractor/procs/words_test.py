# -*- coding: UTF-8 -*-
import words as words
import unittest

WordsProc = words.Words()

class TestExtract(unittest.TestCase) :
    def test1(self) :
	self.assertEqual(WordsProc.solve_keys(u" {{gentilicio2|[[Alemania]]}}. {{plm|alemán}}  {{inflect.es.adj.agudo-cons|catal|á|n}}"),u" gentilicio2 Alemania. alemán  ")

    def test2(self) :
	self.assertEqual(WordsProc.solve_squares(u" [[germánico|germánica]] [[occidental]]  [[w:algo|esto si]]"),u" germánico(germánica) occidental  esto si")

    def test3(self) :
	self.assertEqual(WordsProc.solve_keys_forma(ur" {{forma verbo|translimitar|p=1s|t=futuro|m=subjuntivo|leng=es}}."),ur" forma verbo translimitar persona: 1s tiempo: futuro modo: subjuntivo lengua: Español.")		

if __name__ == '__main__':
    unittest.main()

