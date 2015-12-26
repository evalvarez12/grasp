import extract as ext
import unittest


class TestExtract(unittest.TestCase) :
    
    def test1(self) :
	self.assertEqual(ext.processLine("word1 word2"),["word1","word2"])

    def test2(self) :
	self.assertEqual(ext.processLine("(word?!)"),["word"])
	
    def test3(self) :
	self.assertEqual(ext.processLine(" words ?"),["words"])

    def test4(self) :
	self.assertEqual(ext.processLine("this is a 23241"),["this", "is", "a", "#"])

    def test5(self) :
	self.assertEqual(ext.processLine("some-thing"),["some", "thing"])

    def test6(self) :
	self.assertEqual(ext.processLine(" another-thing ! "),["another", "thing"])
    
    #def test7(self) :
	#self.assertEqual(ext.processLine("some<trash>thing"),["something"])	
	
    #def test8(self) :
	#self.assertEqual(ext.processText("\n<some-html-code>\n "),[])	
	


if __name__ == '__main__':
    unittest.main()

      