import extract as ext
import unittest


class TestExtract(unittest.TestCase) :
    
    def test1(self) :
	self.assertEqual(ext.process("word1 word2"),["word1","word2"])

    def test1(self) :
	self.assertEqual(ext.process("(word?!)"),["word"])
	
    def test1(self) :
	self.assertEqual(ext.process(" words ?"),["words"])

    def test1(self) :
	self.assertEqual(ext.process("this is a 23241"),["this", "is", "a", "#"])

    def test1(self) :
	self.assertEqual(ext.process("some-thing"),["some", "thing"])

    def test1(self) :
	self.assertEqual(ext.process(" another-thing ! "),["another", "thing"])	


if __name__ == '__main__':
    unittest.main()

      