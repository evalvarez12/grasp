import fetch as fet
import unittest


class TestFetch(unittest.TestCase) :
    
    def test1(self) :
	self.assertRaises(fet.getSynonims("arboleda"))




if __name__ == '__main__':
    unittest.main()

      