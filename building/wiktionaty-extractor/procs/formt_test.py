# -*- coding: UTF-8 -*-
import formt as fmt
import unittest

FmtProc = fmt.Format()

class TestExtract(unittest.TestCase) :
    
    def test1(self) :
	self.assertEqual(FmtProc.clean(u"       palabra \t\t  \n\n"),u"palabra \t \n")	
	   
    def test2(self) :
	self.assertEqual(FmtProc.clean(u"::algo  \n;palabra"),u"algo \npalabra")	
	

if __name__ == '__main__':
    unittest.main()

     