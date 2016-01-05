# -*- coding: UTF-8 -*-
import extract as ext
import unittest


class TestExtract(unittest.TestCase) :
    
    def test1(self) :
	self.assertEqual(ext.process_line("one two"),["one","two"])

    def test2(self) :
	self.assertEqual(ext.process_line("(word?!)"),["word"])
	
    def test3(self) :
	self.assertEqual(ext.process_line(" words ..."),["words"])

    def test4(self) :
	self.assertEqual(ext.process_line("this is a 23241"),["this", "is", "a"])

    def test5(self) :
	self.assertEqual(ext.process_line("some-thing"),["some", "thing"])

    def test6(self) :
	self.assertEqual(ext.process_text(" words \n \n new paragraph  \n"),["words", "new","paragraph"])
    
    def test7(self) :
	self.assertEqual(ext.process_line(u'nñ aá eé'),["nñ","aá"])	
	
    #def test8(self) :
	#self.assertEqual(ext.process_text("\n<some-html-code>\n "),[])	
	


if __name__ == '__main__':
    unittest.main()

      